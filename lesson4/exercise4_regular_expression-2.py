"""
Using a named regular expression (?P<name>) extract the model from the below string.

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

Note, in this example '881' is the relevant model. Your regular expression should not, however,
include '881' in its search pattern since this number changes across devices.

Using a named regular expression, also extract the "236544K/25600K" memory string.

Once again none of the actual digits of the memory on this device should be used in the regular
expression search pattern.

Print both the model number and the memory string to the screen.
"""
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''
#解法1
#要查詢的字串(881 和 236544K/25600K):Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
#\S 是指非空格,
match = re.search(r"Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes of memory",show_version,flags=re.M)
if match:
    model = match.group(1)
    memory = match.group(2)
print(f'Cisco model is {model}')
print(f'Cisco memory is {memory}')




#解法2
# obj = re.compile(r"Cisco 881 (?P<cisco1>.*?) processor with (?P<memory>.*?) bytes of memory.",re.S)
# result = obj.finditer(show_version)
# for it in result:
#     print(it.group("cisco1"))
#     print(it.group("memory"))

#解法3
# match = re.search(
#     r"^Cisco (?P<model>\S+).* with (?P<memory>\S+) bytes of memory",
#     show_version,
#     flags=re.M,
# )
# model = match.groupdict()["model"]
# memory = match.groupdict()["memory"]
#
# print()
# print("-" * 80)
# print("Model: {}".format(model))
# print("Memory: {}".format(memory))
# print("-" * 80)
# print()