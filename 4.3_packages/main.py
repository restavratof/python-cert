from sys import path

path.append('modules')  # relative or absolute path

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

print(path)
