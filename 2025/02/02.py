import re

with open("data.txt", "r") as f: 
    num_ranges = [(int(x), int(y)) for x, y in re.findall(r"(\d+)-(\d+)", f.readline())]

id_list = ([], [])

for num_range in num_ranges:
    for num in range(num_range[0], num_range[1]+1):
        num_string = str(num)
        if num_string[:len(num_string)//2] == num_string[len(num_string)//2:]:
            id_list[0].append(num)
        if re.match(r"^(.+)\1+$", num_string):
            id_list[1].append(num)

print(sum(id_list[0]), sum(id_list[1]))