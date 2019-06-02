import math
print(math.sin(math.pi/2))

print('-'*10,'2')
from math import sin,pi
print(sin(pi/2))

print('-'*10,'aliasing:')
import math as M
print(M.sin(M.pi/2))
# after successful execution of an aliased import, the original module name becomes inaccessible and must not be used.

print('-'*10,'aliasing 2:')
from math import sin as sine, pi as P
print(sine(P/2))

#-----------------------------------------------
# Some useful modules
#-----------------------------------------------
print('-'*50)
print(' 4.2')
print('-'*50)
import os
print(dir(os)) # list os module functions in a sorted list
print('-'*10, 'math:')
print(M.e)
# ---
from math import ceil, floor, trunc, factorial, hypot
x=1.4
y=2.6
# ceil(x) - return smallest integer greater or equal to x
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
# floor(x) - return largest integere less than or equal x
print(floor(x), floor(y))
print(floor(-x), floor(-y))
# trunc(x) - the value of x is truncated to an integer
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))
# factorial - returns x! (x has to be an integral and not a negative)
print(factorial(2), factorial(3))
# hypot(x,y)→ returns the length of the hypotenuse of a right-angle triangle
# with the leg lengths equal to x and y (the same as sqrt(pow(x,2)+pow(y,2)) but more precise)
print(hypot(x, y))
print(hypot(-x, -y))
print('-'*50)
print('-'*10, 'random:')
from random import random, seed, randrange, randint, choice, sample
for i in range(5):
    print(random())
print('-'*10, 'random with custom seed:')
seed(0)
for i in range(5):
    print(random())

print('-'*10, 'randrange:')
# randrange(end)
print(randrange(1), end=' ')
# randrange(beg, end)
print(randrange(0, 1), end=' ')
# randrange(beg, end, step)
print(randrange(0,1,1), end=' ')
# randint(left, right)
print(randint(0,0))

print('-'*10, 'choise and sample:')
# choise -  choose a random element from an input sequence and returns it.
#           choice(sequence)
# sample -  builds a list consisting of the elements_to_chose element "drawn" from the input sequesnce
#           sample(sequence, elements_to_chose=1)
lst = [1,2,3,4,5,6,7,8,9,10]
print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))






