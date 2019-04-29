#  list comprehension
print('-'*6, '  list comprehension')
squares = [ x ** 2 for x in range(10) ]
print(squares)
twos = [2 ** i for i in range(8)]
print(twos)
odds = [x for x in squares if x % 2 != 0  ]
print(odds)

print('-'*6, '  Board creation')
# BOARD CREATION
EMPTY = 0
board = []
for i in range(8):
    row = [ EMPTY for i in range(8)]
    board.append(row)
print(board)

print('-'*6, '  Board creation with nested list comprehension')
board = [[ EMPTY for i in range(8)] for j in range(8)]
print(board)

board[0][0] = 'ROOK'
board[0][7] = 'ROOK'
board[7][0] = 'ROOK'
board[7][7] = 'ROOK'
print(board)


print('-'*6, '  Temperature')
temps = [[0.0 for h in range(24)] for d in range(31)]
print(temps)
sum = 0.0
for day in temps:
    sum += day[11]
average = sum/31
print('Average temperature at noon: ', average)

print('-'*6, '  Hotel')
# 3 buildings, 15 floors, 20 rooms
hotel = [[[False for r in range(20)] for f in range(15)] for b in range(3)]
print(hotel)

