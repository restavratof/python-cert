# BaseException ← Exception ← ArithmeticError
#       An abstract exception including all exceptions caused by arithmetic operations
#       like zero division or an argument’s invalid domain
print('-'*5, 'ArithmeticError:')
#----------------------------------------------------------------
# BaseException ← Exception ← AssertionError
#       A concrete exception raised by the assert instruction when
#       its argument evaluates to False, None, zero, or an empty string
print('-'*5, 'AssertionError:')

#----------------------------------------------------------------
# BaseException
#       The most general(abstract) of all Python exceptions – all other exceptions are included in this one;
#       it can be said that the following two except branches are equivalent:
#           except:
#           and
#           except BaseException:
print('-'*5, 'BaseException:')

#----------------------------------------------------------------
# BaseException ← Exception
#       An abstract exception including all exceptions caused by errors resulting from code malfunctions
#       (there are also exceptions that are rooted outside of your code; be alert!)
print('-'*5, 'Exception:')

#----------------------------------------------------------------
# BaseException ← Exception ← LookupError ← IndexError
#       a concrete exception raised when you try to access a non-existent sequence’s element (e.g., a list’s)
print('-'*5, 'IndexError:')

#----------------------------------------------------------------
# BaseException ← KeyboardInterrupt
#       A concrete exception raised when the user uses a keyboard shortcut
#       designed to terminate a program’s execution (Ctrl-C in most OSs);
#       if handling this exception doesn’t lead to program termination, the program continues its execution.
#       Note: this exception is not derived from the Exception class.
print('-'*5, 'KeyboardInterrupt:')

#----------------------------------------------------------------
# BaseException ← Exception ← LookupError
#       An abstract exception including all exceptions caused by errors
#       resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
print('-'*5, 'LookupError:')

#----------------------------------------------------------------
# BaseException ← Exception ← MemoryError
#       A concrete exception raised when an operation cannot be completed due to a lack of free memory
print('-'*5, 'MemoryError:')

#----------------------------------------------------------------
# BaseException ← Exception ← ArithmeticError ← OverflowError
#       A concrete exception raised when an operation produces a number too big to be successfully stored
print('-'*5, 'OverflowError:')
# the code prints subsequent values of exp(k), k = 1,2,4,8,16,…
from math import exp
ex = 1
try:
      while True:
            print(exp(ex))
            ex *= 2
except OverflowError:
      print('Number is too big.')

#----------------------------------------------------------------
# BaseException ← Exception ← StandardError ← ImportError
#       A concrete exception raised when an import operation fails
print('-'*5, 'ImportError:')
try:
      import math
      import time
      import abracadabra
except:
      print('One of your imports has failed. ')

#----------------------------------------------------------------
# BaseException ← Exception ← LookupError ← KeyError
#       A concrete exception raised when you try to access a non-existent collection’s element (e.g., a dictionary’s)
print('-'*5, 'KeyError:')
# how to abuse the dictionary and how to deal with it
dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
      while True:
            ch = dict[ch]
            print(ch)
except KeyError:
      print('No such key:', ch)

