with open("data.txt", "r") as f:
    file: List[Any] = [line.strip() for line in f]
    id_ranges = file[:file.index("")]
    ids = file[file.index("")+1:]

for r, id_range in enumerate(id_ranges):
    dash = id_range.index("-")
    id_ranges[r] = (int(id_range[:dash]), int(id_range[dash+1:])+1)
    
ids = list(map(int, ids))

# Part One
count = 0
for id in ids:
    for id_range in id_ranges:
        if id in range(*id_range):
            count += 1
            break
print(count)

# Part Two
for pos_a, id_range_a in enumerate(id_ranges):
    for pos_b, id_range_b in enumerate(id_ranges):
        if pos_a == pos_b:
            continue
        if id_range_a[0] in range(*id_range_b):
            if id_range_a[1] in range(*id_range_b):
                id_ranges[pos_a] = (0,0)
            else:
                id_ranges[pos_b] = (id_range_b[0], id_range_a[1])
                id_ranges[pos_a] = (0,0)
        elif id_range_a[1] in range(*id_range_b):
            id_ranges[pos_b] = (id_range_a[0], id_range_b[1])
            id_ranges[pos_a] = (0,0)

fresh_ids = sum([id_range[1] - id_range[0] for id_range in id_ranges])
print(fresh_ids)
