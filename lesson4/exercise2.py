"""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.

The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.

The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta

Convert each of these three lists to a set.

Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
"""

huston_ips =[
    "10.10.10.1",
    "10.10.20.1",
    "10.10.30.1",
    "10.10.40.1",
    "10.10.50.1",
    "10.10.60.1",
    "10.10.70.1",
    "10.10.80.1",
    "10.10.10.1",
    "10.10.20.1",
    "10.10.70.1",
]

atlanta_ips = [
    "10.10.10.1",
    "10.10.20.1",
    "10.10.30.1",
    "10.10.140.1",
    "10.10.150.1",
    "10.10.160.1",
    "10.10.170.1",
    "10.10.180.1",
]

chicago_ips = [
    "10.10.10.1",
    "10.10.20.1",
    "10.10.140.1",
    "10.10.150.1",
    "10.10.210.1",
    "10.10.220.1",
    "10.10.230.1",
    "10.10.240.1",
]

huston_ips = set(huston_ips)
atlanta_ips = set(atlanta_ips)
chicago_ips = set(chicago_ips)

print()
print("-" * 80)

print(f'Duplicate IPs at Huston and Atlanta sites: {huston_ips & atlanta_ips}')

print()
print("-" * 80)

print(f'Duplicate IPs at all three sites: {huston_ips & atlanta_ips & chicago_ips}')
print()
print("-" * 80)

print(f'Chicago unique IP addresses: {chicago_ips.difference(huston_ips).difference(atlanta_ips)}')
