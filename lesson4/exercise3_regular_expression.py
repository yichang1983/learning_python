"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.

Your output should look as follows:

          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102

"""

import re

with open('show_version.txt', 'r') as f:
    show_version = f.read()
# print(show_version)

match = re.search(r"^Cisco IOS Software,.* Version (.*),", show_version, flags=re.M)   # show_version 就是內容, flags=re.M 意思是從頭到尾找一次,
# Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
if match:
    os_version = match.group(1)     #.group(1) 就是(.*)的內容

match = re.search(r"^Processor board ID (.*)", show_version, flags=re.M)
if match:
    serial_number = match.group(1)

match = re.search(r"Configuration register is (.*)", show_version, flags=re.M)
if match:
    config_register = match.group(1)

print(f'OS Version: {os_version}')
print(f'Serial Number: {serial_number}')
print(f'Config Register: {config_register}')