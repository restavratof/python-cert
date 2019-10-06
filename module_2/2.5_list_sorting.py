# 8  10  6   2  4
# 8  6   10  2  4
# 8  6   2  10  4
# 8  6   2  4  10
# 6  8   2  4  10
# 6  2   8  4  10
# 6  2   4  8  10
# 2  6   4  8  10
# 2  4   6  8  10


list = [ 8, 10, 6, 2, 4 ]
print('BEFORE: ', list)
# We need 5 - 1 comparison
swapped = True
while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            # If we end up here -> We have to swap elements
            swapped = True
            list[i], list[i+1] = list[i+1], list[i]

print('AFTER: ', list)

