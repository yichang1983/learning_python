"""
寫一個 mac address 轉換表
輸入mac address 則做轉換
c89c.1dea.0eb6 轉成大寫的 C8:9C:1D:EA:0E:B6
"AA:BB:CC:DD:EE:FF" 轉成大寫的 AABB.CCDD.EEFF 或是小寫的 aabb.ccdd.eeff

step1. 輸入mac, 把中間有點的先移除,再把它變成大寫
step2. 每二個字母後面新增一個:
step3. 輸入mac, 把中間有:的先移除,再把它變成大寫和小寫
step4. 每四個字母中間新增一個.
"""
# def mac_address():
#     new_mac = []
#     mac_addr = input("Please insert mac_address:")
#     for mac in mac_addr:
#         mac = mac.replace(".", "")
#         mac = mac.upper()
#         new_mac.append(mac)         #將 mac 添加到 new_mac 列表中
#     new_mac = "".join(new_mac)      #整個迴圈結束後將 new_mac 列表轉換為字串
#     # print(new_mac)
#     standardized_mac = ""
#     for i in range (0, len(new_mac), 2):
#         octet = new_mac[i: i+2]
#         standardized_mac += octet + ":"         # 在每個八位組後添加冒號
#
#     standardized_mac = standardized_mac.rstrip(":")      # 移除末尾多餘的冒號
#     print(f'MAC_address is: {standardized_mac}')
#
# mac_address()
#
# def mac_addreses_1():
#     new_mac_1 =[]
#     mac_addr_1 = input("Please insert mac_address:")
#     for mac in mac_addr_1:
#         mac = mac.replace(":","")
#         new_mac_1.append(mac)           #將 mac 添加到 new_mac_1 列表中
#     new_mac_1 = "".join(new_mac_1)      #整個迴圈結束後將 new_mac_1 列表轉換為字串
#     mac_upper = new_mac_1.upper()
#     mac_lower = new_mac_1.lower()
#     # print(mac_upper)
#     # print(mac_lower)
#
#     standardized_mac = ""
#     for i in range (0, len(mac_upper), 4):
#         octet = mac_upper[i: i+4]
#         standardized_mac += octet + "."
#     # print(standardized_mac)
#     standardized_mac = standardized_mac.rstrip(".")
#     standardized_mac_upper = standardized_mac.upper()
#     standardized_mac_lower = standardized_mac.lower()
#     print(f'Upper MAC address is: {standardized_mac_upper}')
#     print(f'Lower MAC address is: {standardized_mac_lower}')
#
# mac_addreses_1()





def mac_address():
    while True:
        new_mac = []
        mac_addr = input("Please insert mac_address:")
        if "." in mac_addr:
            for mac in mac_addr:
                mac = mac.replace(".", "")
                mac = mac.upper()
                new_mac.append(mac)         #將 mac 添加到 new_mac 列表中
            new_mac = "".join(new_mac)      #整個迴圈結束後將 new_mac 列表轉換為字串
            # print(new_mac)
            standardized_mac = ""
            for i in range (0, len(new_mac), 2):
                octet = new_mac[i: i+2]
                standardized_mac += octet + ":"         # 在每個八位組後添加冒號

            standardized_mac = standardized_mac.rstrip(":")      # 移除末尾多餘的冒號
            standardized_mac_upper = standardized_mac.upper()
            standardized_mac_lower = standardized_mac.lower()

            print(f'Upper MAC_address is: {standardized_mac_upper}')
            print(f'Lower MAC_address is: {standardized_mac_lower}')
            print()
        elif ":" in mac_addr:
            for mac in mac_addr:
                mac = mac.replace(":","")
                new_mac.append(mac)           #將 mac 添加到 new_mac_1 列表中
            new_mac = "".join(new_mac)      #整個迴圈結束後將 new_mac_1 列表轉換為字串
            mac_upper = new_mac.upper()
            mac_lower = new_mac.lower()
            # print(mac_upper)
            # print(mac_lower)

            standardized_mac = ""
            for i in range(0, len(mac_upper), 4):
                octet = mac_upper[i: i+4]
                standardized_mac += octet + "."
            # print(standardized_mac)
            standardized_mac = standardized_mac.rstrip(".")
            standardized_mac_upper = standardized_mac.upper()
            standardized_mac_lower = standardized_mac.lower()
            print(f'Upper MAC address is: {standardized_mac_upper}')
            print(f'Lower MAC address is: {standardized_mac_lower}')
            print()
        else:
            print("The MAC address is not the correct format")
            print()


mac_address()