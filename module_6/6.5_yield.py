inputNumber = 10

print('-'*10)
def fibonacci(max):
    a, b = 0, 1
    for _ in range(max):
        yield a
        a, b = b, a + b

test1 = fibonacci(inputNumber)


print('In column:')
for i in test1:
    print(i)

print('In list:')
print(list(test1))