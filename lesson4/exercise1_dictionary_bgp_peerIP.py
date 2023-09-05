"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.

Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.

Using a for-loop iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""

net_device = {
    "ip_addr": "10.10.10.10",
    "vendor": "cisco",
    "username": "admin",
    "password": "password",
}

print()
print(net_device["ip_addr"])
print()

if net_device["vendor"].lower == "cisco":
    net_device["platform"] = "ios"
elif net_device["vendor"].lower == "juniper":
    net_device["platform"] = "junos"

bgp_field ={
    "bgp_as" : 42,
    "peer_as" : 100,
    "peer_ip" : "172.16.31.100"
}
net_device.update(bgp_field)    #.update function是指把bgp_field 字典的容容加上去原有的字典裡.
print("-" * 80)
for key in net_device:
    print(f'{key}')
print(("-" * 80))
print()

print(("-" * 80))
for key, value in net_device.items():
    print(f'{key}:{value}')
print(("-" * 80))
print()
