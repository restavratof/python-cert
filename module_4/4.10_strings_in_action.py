#--------------------------
# strings can be compared using the same set of operators which are in use in relation to numbers:
#   == != > >= < <=
#   BUT,result may be surprizing. It compares code point values, character by character.
print('-'*5,'COMPARISON:')
print('alpha' == 'alpha')
print('alpha' != 'Alpha')

# The final relation between strings is determined by comparing the first different character in both strings
#   (keep ASCII/UNICODE code points in mind at all times)
# When you compare two strings of different lengths and the shorter one is identical to the longer one’s beginning,
#   the longer string is considered greater.
print('alpha' < 'alphabet')

# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case).
print('beta' > 'Beta')

# Even if a string contains digits only, it’s still not a number. It’s interpreted as-is, like any other regular string

# Comparing strings against numbers is generally a bad idea. Allowed only == and != operators.
print('-'*5,'SORTING:')
greek = ['omega', 'alpha', 'pi', 'gamma']
# sorted() - function takes one argument (a list) and returns a new list, filled with the sorted argument’s elements
#            The original list remains untouched.
print('-'*3,'sorted()')
greek2 = sorted(greek)
print(greek)
print(greek2)

# sort() - faffects the list itself – no new list is created.
#           Ordering is performed in situ by the method named sort()
print('-'*3,'sort()')
greek.sort()
print(greek)

print('-'*5,'CONVERTING:')
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' +sf)

# The reverse transformation (string → number) is possible when and only when the string represents a valid number.
# If the condition is not met, expect aValueError exception.
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
print(itg + flt)

