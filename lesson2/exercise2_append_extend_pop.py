"""Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in
the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
in the list.
"""

my_ipaddress = ["192.168.1.1", "10.10.10.10", "172.16.30.30", "192.168.200.200", "8.8.8.8"]
print(my_ipaddress)
my_ipaddress.append("7.7.7.7")
print(my_ipaddress)
my_ipaddress.extend(["1.1.1.1","2.2.2.2"])
print(my_ipaddress)
my_ipaddress = my_ipaddress + ['3.3.3.3', '4.4.4.4']
print(my_ipaddress)

print(my_ipaddress[0])
print(my_ipaddress[-1])

first_ip = my_ipaddress.pop(0)
last_ip = my_ipaddress.pop()
print(first_ip)
print(last_ip)

print(my_ipaddress)

my_ipaddress[0] = '5.5.5.5'
print(my_ipaddress)