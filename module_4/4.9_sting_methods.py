str1 = 'Hello World'

#--------------------------
# capitalize() - change letters case, 1st -> Upper, others -> lower
print('-'*5,'capitalize()')
print(str1.capitalize())

#--------------------------
# lower() - make a string copy, replace all upper case letters into lower case
print('-'*5,'lower()')
print(str1.lower())

#--------------------------
# upper() - make a string copy, replace all lower case letters into upper case
print('-'*5,'upper()')
print(str1.upper())

#--------------------------
# center() - makes a copy of the original string, trying to center it inside a field of a specified width
print('-'*5,'center()')
print('['+str1.center(5)+']')
print('['+str1.center(30)+']')
print('['+str1.center(30,'*')+']')

#--------------------------
# startswith() – it checks if a given string starts with the specified substring.
print('-'*5,'startwith()')
print(str1.startswith('he'))

#--------------------------
# endswith() method checks if the given string ends with the specified argument and returns True or False
print('-'*5,'endwith()')
print(str1.endswith('ld'))

#--------------------------
# find() - it looks for a substring (like index()),
#       but doesn’t generate an error for an argument containing a non-existent substring (it returns -1 then)
#       works with strings only
#   Note: don’t use find() if you only want to check if a single character occurs within a string
#       – the in operator will be significantly faster.
#   find(CHAR_TO_FIND)
#   find(CHAR_TO_FIND, POSITION_TO_START)
#   find(CHAR_TO_FIND, POSITION_TO_START, FIRST_IGNORED_INDEX)
print('-'*5,'find()')
print('1-',str1.find('l'))
print('2-',str1.find('l',4))
print('3-',str1.find('o',2,5))
print('4-',str1.find('he'))
print('5-',str1.find('LD'))

fnd = str1.find('l')
while fnd != -1:
    print('6-',fnd)
    fnd = str1.find('l', fnd+1)

#--------------------------
# rfind() - similar to find() only, but start their searches from the end of the string
print('-'*5,'rfind()')
print(str1.rfind('o',2,5))

#--------------------------
# isalnum() - checks if the string contains only digits or alphabetical characters (letters), and returns True/False
#      Note: An empty string or any string element that is not a digit or a letter causes the method to return False.
print('-'*5,'isalnum()')
print(str1.isalnum())
str2 = 'Hello1986'
print(str2.isalnum())

#--------------------------
# isalpha() - check if the string contains only letters, and return True/False.
print('-'*5,'isalpha()')
print(str1.isalpha())
print(str2.isalpha())
print('qwerty'.isalpha())

#--------------------------
# isdigit() method looks at digits only – anything else produces False as the result
print('-'*5,'isdigit()')
print(str2.isdigit())
print('12345'.isdigit())

#--------------------------
# islower() - is a fussy variant of isalpha() – it accepts lower-case letters only.
print('-'*5,'islower()')
print(str1.islower())
print(str2.islower())

#--------------------------
# isupper() - is a fussy variant of isalpha() – it accepts upper-case letters only.
print('-'*5,'isupper()')
print(str1.isupper())
print('HELLO'.isupper())

#--------------------------
# isspace() method identifies whitespaces only – it disregards any other character (the result is False then).
print('-'*5,'isspace()')
print(str1.isspace())
print('\n'.isspace())

#--------------------------
# join() - performs a join – it expects one argument as a list;
#    It must be assured that all the list’s elements are strings the method will raise a TypeError exception otherwise;
#    All the list’s elements will be joined into one string but . . .
#    The string from which the method has been invoked is used as a separator, put among the strings;
#    The newly created string is returned as a result.
print('-'*5,'join()')
print('+'.join(['hello', 'silly','world']))


#--------------------------
# lstrip() - returns a newly created string formed from the original one by removing all leading whitespaces
print('-'*5,'lstrip()')
print('['+' tra ta  '.lstrip()+']')
# lstrip('defined_char') - returns a newly created string formed from the original one by removing all leading "defined_chars"
print('www.fata.by'.lstrip('w'))

#--------------------------
# rstrip() - do nearly the same as lstrips, but affect the opposite side of the string.
print('-'*5,'rstrip()')
print('www.fata.by'.rstrip('by'))
print('['+' tra ta  '.rstrip()+']')

#--------------------------
# strip() - it makes a new string lacking all the leading and trailing whitespaces.
print('-'*5,'strip()')
print('www.fata.byw'.strip('w'))
print('['+' tra ta  '.strip()+']')

#--------------------------
# replace() - returns a copy of the original string
#        in which all occurrences  of the first argument have been replaced by the second argument
#       The second argument can be an empty string (replacing is actually removing, then), but the first cannot be.
#       The third argument (a number) - is a limit of replacements numbers
print('-'*5,'replace()')
print('la la, na na'.replace('la', 'ty'))
print('la la, na na'.replace('la', 'ty', 1))

#--------------------------
# split() - splits the string and builds a list of all detected substrings.
#           The method assumes that the substrings are delimited by whitespaces
#           – the spaces don’t take part in the operation, and aren’t copied into the resulting list.
#       If the string is empty, the resulting list is empty too.
#       Note: the reverse operation can be performed by the join() method.
print('-'*5,'split()')
print('pi chi\npsi'.split())

#--------------------------
# swapcase() - makes a new string by swapping the case of all letters within the source string:
#               lower-case characters become upper-case, and vice versa.
print('-'*5,'swapcase()')
print(str1.swapcase())

#--------------------------
# title() - changes every word’s first letter to upper-case, turning all other ones to lower-case.
print('-'*5,'title()')
print('hEllo my friend'.title())




