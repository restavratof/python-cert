numbers = [ 10, 5, 7, 2, 1 ]
print('a: ', numbers)
numbers[0] = 111
print('b: ', numbers)
numbers[1] = numbers[4]
print('c: ', numbers)
print('d: ', len(numbers))
# Remove element
del numbers[1]
print('e: ', numbers)
# The last one
print('f: ', numbers[-1])
# Append element to the end of list
numbers.append(35)
print('g: ', numbers)
# Add new element at certain position   Format: list.insert(where, what)
numbers.insert(0, 222)
print('h: ', numbers)


# Variables swap
print('-'*6,' Variables swap:')
var1 = 11
var2 = 22
print('var1:',var1,', var2:',var2)
var1, var2 = var2, var1
print('var1:',var1,', var2:',var2)

print('-'*6,' Variables swap List:')
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


