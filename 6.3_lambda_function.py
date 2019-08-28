#--------------------------------------
# Declaration:
# lambda parameters : expression
two = lambda : 2
sqr = lambda x:x*x
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end=' ')
    print(pwr(a, two()))


print('-'*20)
#--------------------------------------
print('Standard Functions:')
def printfunction(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

printfunction([x for x in range(-2, 3)], poly)

print('-'*20)
#--------------------------------------
print('Lambda:')
def printfunction(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

printfunction([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

print('-'*20)
#--------------------------------------
print('Lambdas and the map() function:')
# The map() function applies the function passed by its first argument to all its second argument's elements,
#           and returns an iterator delivering all subsequent function results.
list1 = [x for x in range(5)]
list2 = list(map(lambda x: 2 ** x, list1))
print(list2)

for x in map(lambda x: x * x, list2):
    print(x, end=' ')
print()

print('-'*20)
#--------------------------------------
print('Lambdas and the filter():')
# filter()  - expects the same kind of arguments as map(), but does something different
#           - it filters its second argument while being guided by directions flowing from the function specified
#           as the first argument (the function is invoked for each list element, just like in map()).
from random import seed, randint

seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)



#--------------------------------------
print('-'*20,'\n','SANDBOX:', sep='')

x = lambda a, b : a * b
print(x(5, 6))

