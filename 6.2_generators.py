# range() - function is, in fact, a generator, which is (in fact, again) an iterator

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