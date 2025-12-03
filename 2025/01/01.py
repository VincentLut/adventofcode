with open("data.txt", "r") as f:
    lines = [(1 if line[0] == "R" else -1, int(line[1:-1])) for line in f.readlines()]

dial = 50
count_end_on_0 = 0
count_sweep_over_0 = 0

for line in lines:
    for _ in range(line[1]):
        dial = (dial + line[0]) % 100
        if dial == 0: count_sweep_over_0 += 1
    if dial == 0: count_end_on_0 += 1

print(count_end_on_0, count_sweep_over_0)