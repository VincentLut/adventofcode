import numpy as np

field = []
with open("data.txt", "r") as f:
    for line in f:
        field.append([1 if elem == "@" else 0 for elem in line.strip()])
field = np.array(field)
field = np.pad(field, pad_width=1, mode="constant", constant_values=0)

first_count = 0
for row in range(1, field.shape[0]-1):
    for col in range(1, field.shape[1]-1):
        if field[row, col] == 0:
            continue
        if np.sum(field[row-1:row+2, col-1:col+2]) < 5:
            first_count += 1

counter = 0
prev_count = -1
while prev_count != counter:
    prev_count = counter
    for row in range(1, field.shape[0]-1):
        for col in range(1, field.shape[1]-1):
            if field[row, col] == 0:
                continue
            if np.sum(field[row-1:row+2, col-1:col+2]) < 5:
                counter += 1
                field[row, col] = 0

print(first_count, counter)