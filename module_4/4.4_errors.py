#-----------------------------------------
# EXCEPT
#-----------------------------------------
# Don’t forget that:
#     the except branches are searched in the same order in which they appear in the code;
#     you must not use more than one except branch with a certain exception name;
#     the number of different except branches is arbitrary – the only condition is that if you use try, you must put at least one except (named or not) after it;
#     the except keyword must not be used without a preceding try;
#     if any of the except branches is executed, no other branches will be visited;
#     if none of the specified except branches matches the raised exception, the exception remains unhandled (we’ll discuss it soon)
#     if an unnamed except branch exists (one without an exception name), it has to be specified as the last.

try:
	x = int(input())
	y = 1 / x
	print(y)
except ZeroDivisionError:
	print('Cannot divide by zero – sorry!')
except ValueError:
	print('You have to enter an integer value!')
except:
	print('Oh, dear!')
print('THE END')

# Let’s summarize:
#     each raised exception falls into the first matching branch;
#     the matching branch doesn’t have to specify the same exception exactly – it’s enough that the exception is more general (more abstract) than the raised one.

#-----------------------------------------
# RAISE
#-----------------------------------------
# raise EXC1    - raise an EXC1 exception
def badfun(n):
	raise ZeroDivisionError

try:
	badfun(0)
except ArithmeticError:
	print('What did you do?')
print('THE END')


# raise         - re-raise the same exception as currently handled.
#
# There is one serious restriction:
#     this kind of raise instruction may be used inside the except branch only;
#     using it in any other context causes an error.
def badfun(n):
	try:
		return n/0
	except:
		print('I did it again!')
		raise

try:
	badfun(0)
except ArithmeticError:
	print('I see!')
print('THE END')

#-----------------------------------------
# ASSERT
#-----------------------------------------
# How does it work?
#     It evaluates the expression;
#     if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won’t do anything else;
#     otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)
# How it can be used?
#     you may want to put it into your code where you want to be absolutely safe from evidently wrong data, and where you aren’t absolutely sure that the data has been carefully examined before (e.g., inside a function used by someone else)
#     raising an AssertionError exception secures your code from producing invalid results, and clearly shows the nature of the failure;
#     assertions don’t supersede exceptions or validate the data – they are their supplements.

# assert expression
import math
x = float(input())
assert x>=0.0
x = math.sqrt(x)
print(x)



