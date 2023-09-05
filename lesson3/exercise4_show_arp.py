"""
You have the following data structure:
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]
#
# Loop over this data structure and extract all of the MAC addresses. Process all of the MAC
# addresses to get them into a standard format. Print all of the new standardized MAC address to the
# screen. The standardized format should be as follows:
#
# 00:62:EC:29:70:FE
#
# The hex digits should be capitalized. Additionally, there should be a colon between each octet in
# the MAC address.
# """

# 给定 arp_table 数据结构
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')
]


# 循環遍歷 arp_table 並提取 MAC 地址
mac_addresses = []

for ip, mac in arp_table:
    mac = mac.replace('.', '')  # 移除 MAC 地址中的句點（.），以獲取純十六進制字串
    mac = mac.upper()  # 將 MAC 地址轉換為大寫形式

    standardized_mac = ""
    for i in range(0, len(mac), 2):
        octet = mac[i: i+2]  # 每次提取兩個字符，即一個八位組（octet）
        standardized_mac += octet + ":"  # 在每個八位組後添加冒號

    standardized_mac = standardized_mac.rstrip(":")  # 移除末尾多餘的冒號
    mac_addresses.append(standardized_mac)

# 打印標準化的 MAC 地址
for mac_address in mac_addresses:
    print(mac_address)


