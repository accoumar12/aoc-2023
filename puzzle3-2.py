import regex as re

matrix = []
sum = 0

with open("data/puzzle3.csv", "r") as f:
    for line in f:
        elements = [char for char in line if re.match(r"\d|[^\s]", char)]
        matrix.append(elements)

print(matrix)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

positions_matrix = []

for i in range(len(matrix)):
    j = 0
    while j < len(matrix[i]):
        if matrix[i][j].isdigit():
            number = matrix[i][j]
            number_length = 1
            offset = 1
            while (j + offset) < len(matrix[i]) and matrix[i][j + offset].isdigit():
                number_length += 1
                number += matrix[i][j + offset]
                offset += 1
            positions_matrix.append((i, j, int(number), number_length))
            j += number_length
        else:
            j += 1

print(positions_matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "*":
            count = 0
            for 