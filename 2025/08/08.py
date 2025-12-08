from math import dist, prod

with open("data.txt", "r") as file:
    circuits = [[tuple(map(int, line.strip().split(",")))] for line in file]

edges = []
for j1, junct1 in enumerate(circuits):
    for j2, junct2 in enumerate(circuits[j1+1:]):
        edges.append((junct1[0], junct2[0], dist(junct1[0], junct2[0])))

edges = sorted(edges, key=lambda x: x[2])

count = 1
solution = 0
for edge in edges:
    indexes = [-1, -1]
    for c, circuit in enumerate(circuits):
        if edge[0] in circuit: indexes[0] = c
        if edge[1] in circuit: indexes[1] = c
    if indexes[0] != indexes[1]:
        circuits[indexes[1]].extend(circuits[indexes[0]])
        circuits.pop(indexes[0])
        if len(circuits) == 1: 
            solution = edge[0][0] * edge[1][0]
            break
    if count == 1000: 
        lengths = sorted([len(circuit) for circuit in circuits])
    count += 1

print(prod(lengths[-3:]), solution)