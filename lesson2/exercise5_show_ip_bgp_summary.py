"""Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""
banner = "-" * 80

f = open('show_ip_bgp_summary.txt', 'r')
show_ip_bgp_summary = f.read()      # 把show_ip_bgp_summary.txt 變成一個字串
show_ip_bgp_summary = show_ip_bgp_summary.splitlines()      # 用splitline()把它一行一行變成字串
print(show_ip_bgp_summary)
print(banner)

# 抓第一行的字串,結果是:BGP router identifier 10.220.88.20, local AS number 42
first_line = show_ip_bgp_summary[0]
print(first_line)
print(banner)

# 抓第一行的字串的最後一個字,結果是:42
as_number = first_line.split()[-1]
print(f'Local AS is: {as_number}')

print(banner)
print(banner)
# 抓最後一行的字串結果是:10.220.88.38    4           44    7536    8296       59    0    0 5d05h           0
last_line = show_ip_bgp_summary[-1]
print(last_line)
print(banner)

# 抓最後一行的字串的第一個字,結果是:10.220.88.38
peer_ip = last_line.split()[0]
print(f'BGP Peer IP is: {peer_ip}')
