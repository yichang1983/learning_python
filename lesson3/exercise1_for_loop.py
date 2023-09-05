"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]

"""
from pprint import pprint
banner = '-' * 80
vlan_list = []
f = open('show_vlan.txt', 'r')
show_vlan = f.read()

print(show_vlan.splitlines())
print(type(show_vlan))
print(banner)

for line in show_vlan.splitlines():     # 用splitline()把它一行一行變成字串
    if "VLAN" in line or "-----" in line or line.startswith("  "):
        continue
    fields = line.split()    # 如果在 split() 方法中不提供分隔符参数，它将使用默认的空白字符分隔字符串。
    # print(fields)

    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()