# closure - is a technique which allows the storing of values in spite of the fact,
#           that the context in which they have been created does not exist anymore

def outer(par):
	loc = par
	def inner():
		return loc
	return inner

var = 1
fun = outer(var)
print(fun())

# Look carefully:
#     the inner() function returns the value of the variable accessible inside its scope,
#                   as inner() can use any of the entities at the disposal of outer()
#     the outer() function returns the inner() function itself; more precisely, it returns a copy of the inner() function,
#                   the one which was frozen at the moment of outer()'s invocation;
#                   the frozen function contains its full environment, including the state of all local variables,
#                   which also means that the value of loc is successfully retained,
#                   although outer() ceased to exist a long time ago.

# The function returned during the outer() invocation is a closure.


# A closure has to be invoked in exactly the same way in which it has been declared.

print('-'*20)
#--------------------------------------------------------
# It is fully possible to:
#  -  declare a closure equipped with an arbitrary number of parameters, e.g., one, just like the power() function.
#  -  modify its behavior by using values taken from the outside.
#  -  create as many closures as you want using one and the same piece of code.
#       This is done with a function named makeclosure()

def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))


print('-'*20)
#--------------------------------------------------------
# Python program to illustrate
# closures
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	return innerFunction # Note we are returning function WITHOUT parenthesis

if __name__ == '__main__':
	myFunction = outerFunction('Hey!')
	print('---')
	myFunction()


print('-'*20)
#--------------------------------------------------------
# Python program to illustrate
# closures
def logger(func):
	def log_func(*args):
		print('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args))
	# Necessary for closure to work (returning WITHOUT parenthesis)
	return log_func

def add(x, y):
	return x + y

def sub(x, y):
	return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)





# https://realpython.com/primer-on-python-decorators/
