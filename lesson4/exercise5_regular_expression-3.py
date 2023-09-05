import re
with open("show_ipv6_intf.txt","r") as f:
    show_ipv6_intf = f.read()
# print(show_ipv6_intf)

matches = re.findall(r"IPv6 address:\s+(\S+)\s+\[VALID]\n\s+(\S+)", show_ipv6_intf, flags=re.M)
# matches = re.findall(r"IPv6 address:\s+(\S+)\s+\[VALID\]\n\s+(\S+)", show_ipv6_intf, flags=re.M)

for match in matches:
    ipv6_1 = match[0]
    ipv6_2 = match[1]
    print(ipv6_1)
    print(ipv6_2)







# import re
#
# with open("show_ipv6_intf.txt", "r") as f:
#     show_ipv6_intf = f.read()
#
# # IPv7 MTU:: 这部分直接匹配文本中的 "IPv7 MTU:"。
# # \s+: 这部分匹配一个或多个空格字符，以允许在 "IPv7 MTU:" 后有任意数量的空格。
# # (\d+): 这是一个捕获组，用于捕获一个或多个数字字符（即 MTU 值）。\d+ 表示匹配一个或多个数字。
# # .*\n\s+: 这部分匹配零个或多个字符直到换行符，然后再匹配一个或多个空格。
# # (\d+): 这是另一个捕获组，用于捕获最后一行的数字。
# # show_ipv6_intf, flags=re.M): 这是正则表达式的目标文本，即你要从中查找匹配项的文本。flags=re.M 是标志参数，表示启用多行匹配模式，以便 ^ 和 $ 可以匹配每一行的开头和结尾。
# matches = re.findall(r"IPv7 MTU:\s(\S+).*\n\s+(\S+)", show_ipv6_intf, flags=re.M)
# for match in matches:
#     mtu_1 = match[0]
#     mtu_2 = match[1]
#     print(mtu_1)
#     print(mtu_2)
