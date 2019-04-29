# SLICES
# list[start:end]
#     start - first element included into slice
#     end   - last element not included in the slice
from warnings import catch_warnings

print('-'*6,' Slices')
list = [10, 8, 6, 4, 2]
new_list = list[1:3]
print(new_list)
# negative
new_list = list[1:-1]
print(new_list)
# if the start further than emd -> slice will be empty
new_list = list[-1:3]
print(new_list)
# If you omit start element, slice will start with the first element (index 0)
new_list = list[:3]
print(new_list)
# If you omit end element, slice will end with the last element (index len(list))
new_list = list[3:]
print(new_list)
# Omitting both start and end makes a copy o fthe list
new_list = list[:]
print(new_list)

print('-'*6,' Slices del')
# del can delete slices too
del new_list[1:3]
print(new_list)
del new_list[:]
print(new_list)
# del without slice will delete list itself, not only it's content
new_list = list[:]
del new_list
try:
    print(new_list)
except NameError:
    print('NameError: List does not exist!')

print('-'*6,' in')
print(5 in list)
print(4 in list)
print(3 not in list)











