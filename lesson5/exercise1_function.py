"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
"""

def ssh_conn(ip_addr, username, password):
    print(f'ip_addr: {ip_addr}')
    print(f'username: {username}')
    print(f'password: {password}')

ssh_conn('192.168.1.1', 'cisco', 'cisco123')
