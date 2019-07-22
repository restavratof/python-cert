# 1
class MyZeroDivisionError(ZeroDivisionError):
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some worse news")
	else:
		raise ZeroDivisionError("some bad news")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('Division by zero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('My division by zero')
	except ZeroDivisionError:
		print('Original division by zero')


#---------------------------------------------------------
# 2:
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(message)
        self.pizza = pizza

class ToMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese



