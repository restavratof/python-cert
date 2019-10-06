print('-'*9, ' TUPLES')
#empty tiple
tuple3 = ()
# one-element tuple has to be distinguishable from an ordinary, single value, you must end the value with a comma
tuple1 = (1.,)
tuple2 = 1.,

tuple3 = (1,2,4,8)
tuple4 = 1., .5, .25, .125

print(tuple3[0])
print(tuple3[-1])
print(tuple3[1:])
print(tuple3[:-2])
# Tuples are immutable
# You can not add or modify tuple elements after it is defined
print(tuple3 + tuple4)
print(tuple3 * 3)
print(1 in tuple3)
print(5 not in tuple3)

print('-'*9, ' DICTIONARIES')






