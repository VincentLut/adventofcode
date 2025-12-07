arr: List[Any] = [list(line.strip()) for line in open("data.txt", "r")]
for r, row in enumerate(arr):
    for c, col in enumerate(row):
        if col == "^": continue
        elif col == ".": arr[r][c] = 0
        elif col == "S": arr[r][c] = 1

splits_count = 0
for r, row in enumerate(arr):
    if r == 0: continue
    for c, col in enumerate(row):
        if type(arr[r-1][c]) == int and arr[r-1][c] > 0:
            if col == "^":
                arr[r][c-1] += arr[r-1][c]
                arr[r][c+1] += arr[r-1][c]
                splits_count += 1
            else:
                arr[r][c] += arr[r-1][c]

print(splits_count, sum(arr[-1]))