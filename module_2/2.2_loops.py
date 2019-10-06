# While
print("WHILE LOOP:")
i = 0
while i < 5:
    i += 1
print("i:{}".format(i))

print('* With else:')
##########################################
# else - always executed once, regardles of wheter the loop has entered it's body or not
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print('else:',i)
# 1 2 3 4 else:5



print('-'*40)
print("FOR LOOP:")
for i in range(5):
    print(i)

# the range() function (this is a very special function)
# is responsible for generating all the desired values of the control variable;
# in our example, the function will create (we can even say that it will feed the loop with) subsequent values from the following set: 0, 1, 2, 3, 4;
# note: in this case, the range() function starts its job from 0 and finishes it one step (one integer number) before the value of its argument;


# range(FIRST_NOT_ASSIGNED_VALUE)
# range(INITIAL_VALUE, FIRST_NOT_ASSIGNED_VALUE)
# range(INITIAL_VALUE, FIRST_NOT_ASSIGNED_VALUE, INCREMENT)
# Examples:
#   range(5)
#       0 1 2 3 4
#   range(2, 8)
#       2 3 4 5 6 7
#   range(2,8,3)
#       2 5
#   range(1,1)
#       nothing
#   range(2,1)
#       nothing


##########################################
# break     - exit loop immediately
# continue  - go to next turn immediately




