from pprint import pprint

matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

matrix_t = list(zip(*matrix))  # непосредственно транспонирование

pprint(matrix)
print('')
pprint(matrix_t)

# Вывод:
# [[0.5, 0, 0, 0, 0],
#  [1, 0.5, 0, 0, 0],
#  [1, 1, 0.5, 0, 0],
#  [1, 1, 1, 0.5, 0],
#  [1, 1, 1, 1, 0.5]]
#
# [[0.5, 1, 1, 1, 1],
#  [0, 0.5, 1, 1, 1],
#  [0, 0, 0.5, 1, 1],
#  [0, 0, 0, 0.5, 1],
#  [0, 0, 0, 0, 0.5]]

