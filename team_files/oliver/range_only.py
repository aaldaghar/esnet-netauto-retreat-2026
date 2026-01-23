import ipaddress
import os
import json

FILES = "/Users/oliver/src/esnet-netauto-retreat-2026/exercise_files"
prefix_list = []

config_path = os.path.join(FILES, "ipls.json")

with open(config_path, 'r') as file:
            prefix_dict = json.load(file)

for entry in prefix_dict.values():
        for v in entry.values():
            for dict in v:
                prefix = dict.get('ip_prefixes')
                prefix_type = dict.get('type')

                if prefix_type == 'range':
                    prefix_list.append(prefix)
              

print() 
print (f"A total of {len(prefix_list)} prefixes with type = 'range' have been found: {prefix_list}")
print()

