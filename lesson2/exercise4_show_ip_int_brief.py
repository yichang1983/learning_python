"""Read in the "show_ip_int_brief.txt" file into your program using the
.readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can
just hard-code the index at this point since we haven't covered for-loops
or regular expressions:

Use the string .split() method to obtain both the IP address and the
corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need
to 'pip install pycodestyle' on your computer (should be able to type this from
the shell prompt). Alternatively, you can type:

  'python -m pip install pycodestyle'.

"""
banner = '-' * 80
f = open('show_ip_int_brief.txt', 'r')
show_ip_int_brief = f.readlines()
print(show_ip_int_brief)
print(type(show_ip_int_brief))
print(banner)

fa4_ip = show_ip_int_brief[5].strip()   # strip 刪除左邊和右邊空白
print(fa4_ip)
print(type(fa4_ip))
print(banner)

fields = fa4_ip.split()     # 如果在 split() 方法中不提供分隔符参数，它将使用默认的空白字符分隔字符串。
print(fields)
print(banner)

intf = fields[0]
ip_address = fields[1]

my_results = (intf, ip_address)
print(f'結果是:{my_results}')