banner = "-" * 80
f = open('show_version.txt', 'r')
show_ver = f.read()

print(banner)
print(show_ver)
print(type(show_ver))
print(banner)
f.close()
