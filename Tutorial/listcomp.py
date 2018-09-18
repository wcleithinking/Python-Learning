# -*- coding: utf-8 -*-

# Example 1
# case 1
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# case 2
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# case 3
squares = [x**2 for x in range(10)]
print(squares)

# Example 2
# case 1
test = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(test)
# case 2
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x, y))
print(combs)
# case 3
combs = []
for y in [3,1,4]:
    for x in [1,2,3]:
        if x!=y:
            combs.append((x, y))
print(combs)

# Example 3
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x>=0])
print([abs(x) for x in vec])
freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# Example 4
from math import pi
print([str(round(pi,i)) for i in range(1,6)])

# Example 5
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# case 1
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])
# case 2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
# case 3
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
# case 4
print(*matrix)
print(list(zip(*matrix)))
