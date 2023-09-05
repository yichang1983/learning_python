"""
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
"""

f = open('show_lldp_neighbor_detail.txt','r')

found1 = False
found2 = False

show_lldp_neighbor = f.read()
# print(show_lldp_neighbor)
# print(type(show_lldp_neighbor))

for line in show_lldp_neighbor.splitlines():
    if 'System Name' in line:
        system_name = line.split('System Name: ')[1].strip()  # 使用下划线来忽略 split 函数返回的列表中的第一个元素
        print(system_name)
        # _, system_name = line.split("System Name: ")
        found1 = True
        continue
    elif 'Port id' in line:
        # _, port_id = line.split('Port id:')
        port_id = line.split('Port id:')[1].strip()  # 使用下划线来忽略 split 函数返回的列表中的第一个元素
        print(port_id)
        found2 = True
        continue
    if found1 and found2 == True:
        break
print('*' * 80)
print(f'system name: {system_name}')
print(f'port id : {port_id}')
