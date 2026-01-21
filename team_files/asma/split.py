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
    '''
    write your code!!
    '''

def main():
    print_split()

if __name__ == "__main__":
    main()