#----------------------------------------------------------------
# \n   - line feed   - LF

print('a'*3)
print(3*'a')


#----------------------------------------------------------------
# ord() - to know specific character’s ASCII/UNICODE code point value
#           requires one character string or TypeError exception
print('-'*5, 'ord():')
c1 = 'a' # english a
c2 = 'а' # russian a
print(ord(c1))
print(ord(c2))

#----------------------------------------------------------------
# chr() - retunr character by code point number
#           negative or invalid code point will causes ValueError or TypeError exceptions.
print('-'*5, 'chr():')
print(chr(101))    # e
print( chr(ord('x')) == 'x' )

#----------------------------------------------------------------
# Python’s strings are sequences
print('-'*5, 'Python strings are sequences:')
str1 = 'silly walks'

# loop through string
for ch in range(len(str1)):
    print(str1[ch], end=' ')
print()

# iterating
for ch in (str1):
    print(ch, end=' ')
print()

# negative works either. Return character from end
print(str1[-2])

# slices works either
print(str1[6:10])

# in works too
print('w' in str1)
print('c' not in str1)

# You can not
#   - remove character from string. It is immutable
#   - append it or expand in any way (insert will fail too)

#----------------------------------------------------------------
# min() - finds the minimum element of the sequence passed as an argument. (based on ASCII table)
# max() - finds the maximum element of the sequence passed as an argument. (based on ASCII table)
#         the sequence (string, list, it doesn’t matter) cannot be empty, or else you’ll get a ValueError exception.
print('-'*5, 'min() and max():')
print(min(str1))
print(max(str1))

#----------------------------------------------------------------
# index() - method returns the index of the first occurrence of the argument ( min=0, max=len()-1 )
print('-'*5, 'index():')
print(str1.index('a'))


#----------------------------------------------------------------
# list() - create a list from many entities (string, typles, dictionaries...)
print('-'*5, 'list():')
print(list(str1))

#----------------------------------------------------------------
print('-'*5, 'count(l):')
print(str1.count('l'))
