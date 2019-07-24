# list comprehension - a simple and very impressive way of creating lists and their contents.

# creating a list containing a few of the first natural powers of ten.
# 1 - Way with FOR
listOne = []
for ex in range(6):
    listOne.append(10 ** ex)

# 2 - Way with LIST COMPREHENSIONS
listTwo = [10 ** ex for ex in range(6)]

print(listOne)
print(listTwo)

print('-'*20)
#--------------------------------------
# conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.
#   EXPRESSION_ONE if CONDITION else EXPRESSION_TWO
lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)
print(lst)

lst2 = [1 if x % 2 == 0 else 0 for x in range(10)]
print(lst2)

print('-'*20)
#--------------------------------------


print('-'*20)
#--------------------------------------


