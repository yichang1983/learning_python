"""
Create a function that randomly generates an IP address for a network. The default base network
should be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use:

import random
random.randint(1, 254)

to randomly generate the last octet.

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
"""

# import random
# # ip = random.randint(1,254)
# def ip(ip):
#     print(f'IP address is 10.10.10.{ip}')
#
# ip(random.randint(1,254))


import random
def ip_addr(network="10.10.10."):
    last_octet = str(random.randint(1, 254))
    return network + last_octet

print(ip_addr("192.168.5."))


