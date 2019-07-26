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
