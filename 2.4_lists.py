numbers = [ 10, 5, 7, 2, 1 ]
print('-'*3)
print(numbers)

print('-'*3)
numbers[0] = 111
print(numbers)

print('-'*3)
numbers[1] = numbers[4]
print(numbers)
print(len(numbers))

print('-'*40)
print('Remove element on position "1":')
del numbers[1]
print(numbers)

print('Return the Last element:')
print(numbers[-1])

print("Append element to the end of list (35):")
numbers.append(35)
print(numbers)

# Add new element at certain position   Format: list.insert(where, what)
print('Add "222" on position "0":')
numbers.insert(0, 222)
print(numbers)

print('-'*40)
print('VARIABLES SWAP:')
var1 = 11
var2 = 22
print('var1:',var1,', var2:',var2)
var1, var2 = var2, var1
print('var1:',var1,', var2:',var2)

print('-'*6)
print('Variables swap List:')
list = [ 1, 2, 3, 4, 5 ]
print('before:', list)
list[0], list[4] = list[4], list[0]
list[1], list[3] = list[3], list[1]
print('after:', list)

list = [ 1, 2, 3, 4, 5 ]
l = len(list)
print('before:', list)
for i in range(l // 2):
    list[i], list[l - i - 1] = list[l - i - 1], list[i]
print('after:', list)


