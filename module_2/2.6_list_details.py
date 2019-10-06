# SLICES
# list[start:end]
#     start - first element included into slice
#     end   - last element not included in the slice
from warnings import catch_warnings

print('-'*40)
print('SLICES:')
list = [10, 8, 6, 4, 2]
print('* Initial list:')
print('\t',list)

print('* Slice [1:3]:')
new_list = list[1:3]
print('\t',new_list)

print('* Slice [1:-1]:')
new_list = list[1:-1]
print('\t',new_list)

print('* Slice [-1:3]:')
# if the start further than end -> slice will be empty
new_list = list[-1:3]
print('\t',new_list)

print('* Slice [:3]:')
# If you omit start element, slice will start with the first element (index 0)
new_list = list[:3]
print('\t',new_list)

print('* Slice [3:]:')
# If you omit end element, slice will end with the last element (index len(list))
new_list = list[3:]
print('\t',new_list)

print('* Slice [:]:')
# Omitting both start and end makes a copy o fthe list
new_list = list[:]
print('\t',new_list)

print('-'*40)
print('DELETE SLICES:')
# del can delete slices too
print('* Delete slice [1:3]:')
del new_list[1:3]
print('\t',new_list)

print('* Delete slice [:]:')
del new_list[:]
print('\t',new_list)

print('* Delete without slice (WILL DELETE LIST ITSELF):')
# del without slice will delete list itself, not only it's content
new_list = list[:]
del new_list
try:
    print('\t', new_list)
except NameError:
    print('NameError: List does not exist!')











