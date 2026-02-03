import ipaddress
import json
from pathlib import Path
import sys

'''
write `team_files/<your-name>/split.py` that reads `exercise_files/ipls.json`, iterates all entries, and separates IPv4 and IPv6 prefixes.
'''
def read_ipls_json():
    """Read and return the parsed JSON from exercise_files/ipls.json.

    Returns the parsed JSON (dict) or None on error.
    """
    repo_root = Path(__file__).resolve().parents[2]
    ipls_path = repo_root / "exercise_files" / "ipls.json"
    if not ipls_path.exists():
        print(f"ERROR: {ipls_path} not found", file=sys.stderr)
        return None
    try:
        text = ipls_path.read_text()
        return json.loads(text)
    except Exception as e:
        print(f"ERROR: failed to read/parse {ipls_path}: {e}", file=sys.stderr)
        return None

def print_split():
    data = read_ipls_json()
    if data is None:
        return
    ipl_v6_list = []
    ipl_v4_list = []
    
    ipl_data = data.get('ipl', {})
    for ipl_name, elements in ipl_data.items():
        for entry in elements:
            prefixes = entry.get('ip_prefixes')
    
            try:
                check_ip_address = ipaddress.ip_network(prefixes, strict=False)
                if check_ip_address.version == 4:
                    ipl_v4_list.append({
                        'ipl_name' : ipl_name,
                        'ipl_prefixes' : prefixes
                    })
                elif check_ip_address.version == 6:
                    ipl_v6_list.append({
                        'ipl_name' : ipl_name,
                        'ipl_prefixes' : prefixes
                    })
            except ValueError as err:
                print(f'Error in {prefixes} in {ipl_name}: {err}')
    print(f'\n****Here are the Results!****')
    print(f'\n{'*'*80}')
    print(f'{'*'*80}')
    print(f'There are {len(ipl_v4_list)} IPLs with IPv4 only')
    for item in ipl_v4_list:
        print(f'{item['ipl_name']} : {item['ipl_prefixes']}' )
    print(f'\n{'='*80}')
    print(f'There are {len(ipl_v6_list)} IPLs with IPv6 only')
    for item in ipl_v6_list:
        print(f'{item['ipl_name']} : {item['ipl_prefixes']}' )
    print(f'\n{'='*80}')


def main():
    print_split()

if __name__ == "__main__":
    main()