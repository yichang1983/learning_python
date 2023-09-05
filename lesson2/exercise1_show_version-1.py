banner = '-' * 80
with open('show_version.txt') as f:
    show_ver = f.readlines()
print(banner)
print(show_ver)
print(banner)
print(type(show_ver))
print(banner + '\n')