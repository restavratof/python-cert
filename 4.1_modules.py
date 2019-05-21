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
