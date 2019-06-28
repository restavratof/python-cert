class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

so1 = Stack()
so2 = Stack()

so1.push(3)
so1.push(2)
so1.push(1)

so2.push(4)
so2.push(5)

print(so1.pop())
print(so1.pop())
print(so1.pop())
print(so2.pop())

print('--------------')

so3 = AddingStack()
for i in range(5):
    so3.push(i)
print(so3.getSum())

for i in range(5):
    print(so3.pop())

