"""
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
"""
# from pprint import pprint
# arp_list = []
# f = open('show_arp.txt', 'r')
# show_arp = f.read()
# # pprint(show_arp
# for line in show_arp.splitlines():
#     # print(line)
#     fields = line.split()
#     # print(fields)
#
#     if '10.220.88.1' in line:
#         arp_address = fields[1]
#         arp_mac = fields[3]
#         arp_list.append((arp_address, arp_mac))
#     elif '10.220.88.30' in line:
#         arp_address = fields[1]
#         arp_mac = fields[3]
#         arp_list.append((arp_address, arp_mac))
#
# print()
# pprint(arp_list)
##############################################

from pprint import pprint
found1 = False
found2 = False

f = open('show_arp.txt', 'r')
show_arp = f.read()
# pprint(show_arp)
for line in show_arp.splitlines():
    if 'Protocol' in line:
        continue
    fields = line.split()       # 如果在 split() 方法中不提供分隔符参数，它将使用默认的空白字符分隔字符串。
    # print(fields)
    # print(type(fields))
    ip_addr = fields[1]
    mac_addr = fields[3]
    if '10.220.88.1' == ip_addr:
        print(f'Default gateway IP is {ip_addr} and Mac address is {mac_addr} ')
        found1 = True
    elif '10.220.88.30' in ip_addr:
        print(f'Arista3 IP is {ip_addr} and Mac address is {mac_addr}')
        found2 = True
    if found1 and found2:
        print("Exiting...")
        break
print()
