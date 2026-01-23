import ipaddress
import os
import json
import pprint

FILES = "/Users/oliver/src/esnet-netauto-retreat-2026/exercise_files"
v4_list = []
v6_list =  []

config_path = os.path.join(FILES, "ipls.json")

with open(config_path, 'r') as file:
            prefix_dict = json.load(file)

for entry in prefix_dict.values():
        for v in entry.values():
            for dic in v:
                prefix = dic.get('ip_prefixes')
                ip = prefix.split('/')
                try:
                    if ipaddress.ip_address(ip[0]).version == 4:
                        v4_list.append(prefix)
                    elif ipaddress.ip_address(ip[0]).version == 6:
                        v6_list.append(prefix)
                except ValueError as err:
                    print ('*' *55)
                    print (f"INFO: '{prefix}' is not a valid prefix value.")
                    print ('*' *55)

print()
print ("List of V4 prefixes: ",v4_list)
print("List of V6 prefixes: ",v6_list)
print()