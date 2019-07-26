import sys
# range() - function is, in fact, a generator, which is (in fact, again) an iterator

# An iterator must provide two methods:
#
#     __iter__() which should return the object itself and which is invoked once
#               (it's needed for Python to successfully start the iteration)
#
#     __next__() which is intended to return the next value (first, second, and so on) of the desired series
#               - it will be invoked by the for/in statements in order to pass through the next iteration;
#               if there are no more values to provide, the method should raise the StopIteration exception.

#----------------------------------------
# the iterator object is instantiated first;
# next,
# Python invokes the __iter__ method to get access to the actual iterator;
# the __next__ method is invoked eleven times - the first ten times produce useful values, while the eleventh terminates the iteration.
#----------------------------------------
# yield  -  statement has some very interesting effects.
#           First of all, it provides the value of the expression specified after the yield keyword, just like return,
#           but doesn't lose the state of the function.

print('-'*10)
print('Fibonacci Numbers Generator:')
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)


print('-'*10)
#----------------------------------------
# Genrator Fibonacci
inputNumber = 10

print('-'*10)
def fibonacci(max):
    a, b = 0, 1
    for _ in range(max):
        yield a
        a, b = b, a + b

print('In column:')
for i in fibonacci(inputNumber):
    print(i)

print('In list:')
print(list(fibonacci(inputNumber)))


