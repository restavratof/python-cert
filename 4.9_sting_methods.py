str1 = 'hello WORLD'

#--------------------------
# capitalize() - change letters case, 1st -> Upper, others -> lower
print('-'*5,'capitalize()')
print(str1.capitalize())

#--------------------------
# center() - makes a copy of the original string, trying to center it inside a field of a specified width
print('-'*5,'center()')
print('['+str1.center(5)+']')
print('['+str1.center(30)+']')
print('['+str1.center(30,'*')+']')

#--------------------------
# endswith() method checks if the given string ends with the specified argument and returns True or False
print('-'*5,'endwith()')
print(str1.endswith('LD'))





