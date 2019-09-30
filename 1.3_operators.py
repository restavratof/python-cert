#------------------------------------------------------------
# Order
#------------------------------------------------------------
#   ! ~ (type) ++ -- + -       | unary
#   * / %                      |
#   + -                        | binary
#   << >>
#   < <= => >
#   == !=
#   &
#   |
#   &&
#   ||
#   = += -= *= /= %= &= ^= |=  >>= <<=
#------------------------------------------------------------

print('-'*50)
print('NUMERIC OPERATORS:')
print('-'*50)
print('Exponentiation (**):')       # right-sided binding
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print('Multiplication (*):')        # left-sided binding
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print('Division (/):')              # left-sided binding
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print('Integer division (//):')     # left-sided binding
print(6 // 4)
print(6 // 4.)
print(6. // 4)
print(6. // 4.)
print('Remainder (modulo) (%):')    # left-sided binding
print(14 % 4)
print(14 % 4.)
print(14. % 4)
print(14. % 4.)
print('Addition (+):')              # left-sided binding
print(2 + 3)
print(2 + 3.)
print(2. + 3)
print(2. + 3.)
print('Division (-):')              # left-sided binding
print(2 - 3)
print(2 - 3.)
print(2. - 3)
print(2. - 3.)
#------------------------------------------------------------

print('-'*50)
print('BITWISE OPERATORS:')
print('-'*50)
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

# x << y    -     Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
print('Shift to left (x << y):')
print(a << 2)   # 240 = 1111 0000

# x >> y    -     Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
print('Shift to right (x >> y):')
print(a >> 2)   # 15 = 0000 1111

# x & y     -     Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
print('Bitwise AND (x & y):')
print(a&b)      # 12 = 0000 1100

# x | y     -     Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
print('Bitwise OR (x | y):')
print(a|b)       # 61 = 0011 1101

# x ^ y     -     Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
print('Bitwise exclusive OR (x ^ y):')
print(a^b)      # 49 = 0011 0001

# ~ x       -     Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
print('Complement of x ( ~ x):')
print(~ a)       # -61 = 1100 0011
