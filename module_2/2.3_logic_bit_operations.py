# False(0)  True(not 0)
#
##########################################################
# LOGICAL:
##########################################################
#----------------------------------------------
# Left   #  Right   #  AND    #  OR
#----------------------------------------------
# False  # False    # False   # False
# False  # True     # False   # True
# True   # False    # False   # True
# True   # True     # True    # True
#----------------------------------------------


##########################################################
# BITWISE:
##########################################################
# bitwise operators:
#     &     (ampersand)     bitwise conjunction
#     |     (bar)           bitwise disjunction
#     ~     (tilde)         bitwise negation
#     ^     (caret)         bitwise exclusive or (xor)

#----------------------------------------------
# Left   #  Right  #  &   #  |   #  ^
#----------------------------------------------
# 0      # 0       #  0   #  0   #  0
# 0      # 1       #  0   #  1   #  1
# 1      # 0       #  0   #  1   #  1
# 1      # 1       #  1   #  1   #  0
#----------------------------------------------


##########################################################
# EXAMPLES:
##########################################################
# i = 15
# j = 22
# i = 0000000000000000000000000001111
# j = 0000000000000000000000000010110
# ------------------------------------------------------
# log = i and j = True
# logneg = not i = False

# ------------------------------------------------------
# bit = i & j
# bit = 0000000000000000000000000000110
# bitneg = ~i = 1111111111111111111111111110000
#

# ------------------------------------------------------
# Required bit is marked with "x"
# FlagRegister : 000000000000000000000000000x000
# -----------------
# check the state of your bit:
#     X & 1 = x
#     X & 0 = 0
#
# bit mask - a sequence of zeros and ones, whose task is to grab the value or to change the selected bits
# Mask to detect the state of required bit: TheMask = 8
# If FlagRegister & TheMask:
#      Required bit is set
# else:
#      Required bit is reset
#
# -----------------
# Reset required bit
# FlagRegister = FlagRegister & ~TheMask
# or
# FlagRegister &= ~TheMask
#
# -----------------
# Set required bit
# FlagRegister = FlagRegister | TheMask
# or
# FlagRegister |= TheMask
#
# -----------------
# Negate required bit
#      x ^ 1 = ~x
#      x ^ 0 = x
# FlagRegister = FlagRegister ^ TheMask
# or
# FlagRegister ^= TheMask


# ------------------------------------------------------
# SHIFTING  (applied only to integer, not a floats)
#
#     Operators: << and >>
#     [Integer value whose bits are shifted.] [Operator] [Size of the shift]
#
#     Value >> Bits
#     Value << Bits
print("-"*6," SHIFTING:")
Var = 17
VarRight = Var >> 1   # shifting to the right by one bit is the same as integer division by two. E.g. 17 // 2 -> 8
VarLeft = Var << 2    # shifting to the left by two bits is the same as integer multiplication by four. E.g. 17 * 4 -> 68
print(Var, VarRight, VarLeft)