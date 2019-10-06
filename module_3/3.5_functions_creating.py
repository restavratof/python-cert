print('-'*10, 'Body ')
def lb_to_kg(lb):
    return lb * 0.45359237

def ftintom(ft, inch=0.0):
    return  ft * 0.3048 + inch * 0.0254

def BMI(weight, height):
    if (height < 1.0 or height > 2.5) or (weight <20 or weight > 200):
        return None
    return weight/height**2

print(BMI(52.5,1.65))

print(ftintom(1,1))
print(ftintom(6,0))
print(BMI(lb_to_kg(176),ftintom(5,7)))
##########################################################
print('-'*10, 'Factorials')
def Factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * Factorial(n-1)

for i in range(1,6):
    print(i,' - ',Factorial(i))

print('-'*10, 'Fibonacci')
# every subsequent number is the sum of the two preceding numbers
def Fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return Fib(n-1) + Fib(n-2)

print(Fib(3))





