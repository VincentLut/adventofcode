from math import prod

with open("data.txt", "r") as f:
    table = [list(line[:-1]) for line in f]
    numbers = table[:-1]
    sign_indexes = [c for c, char in enumerate(table[-1]) if char != " "]
    signs = [table[-1][c] for c in sign_indexes]
    sign_indexes.append(len(table[-1])+1) # to prevent indexing errors below

num_blocks = []
for i, index in enumerate(sign_indexes[:-1]):
    num_block = [row[index:sign_indexes[i+1]-1] for row in numbers]
    num_blocks.append(num_block)

total_sum_a = 0
total_sum_b = 0
for s, sign in enumerate(signs):
    num_block = [int("".join(row)) for row in num_blocks[s]]
    if sign == "+": total_sum_a += sum(num_block)
    if sign == "*": total_sum_a += prod(num_block)
    
    num_block = [int("".join(row)) for row in zip(*num_blocks[s])]
    if sign == "+": total_sum_b += sum(num_block)
    if sign == "*": total_sum_b += prod(num_block)
print(total_sum_a, total_sum_b)
