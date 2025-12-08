from math import prod, sqrt
from operator import itemgetter

with open("08.txt") as f:
    coords = [[int(i) for i in x.split(",")] for x in f]

n_nodes = len(coords)

distances = []
for i in range(n_nodes):
    for j in range(i + 1, n_nodes):
        dist = sqrt(
            (coords[i][0] - coords[j][0])**2 +
            (coords[i][1] - coords[j][1])**2 +
            (coords[i][2] - coords[j][2])**2
        )
        distances.append(((i, j), dist))

distances.sort(key=itemgetter(1))

clustering = [{i} for i in range(n_nodes)]

for idx, ((n1, n2), _) in enumerate(distances):
    curr = []
    s1 = None
    s2 = None
    
    for s in clustering:
        if n1 in s or n2 in s:
            if n1 in s:
                s1 = s
            if n2 in s:
                s2 = s
        else:
            curr.append(s)
    
    if s1 == s2:
        curr.append(s1)
    else:
        curr.append(s1.union(s2))
    
    if idx == 1000:
        cluster_sizes = sorted([len(c) for c in clustering])
        print(prod(cluster_sizes[-3:]))
    
    clustering = curr
    
    if len(clustering) == 1:
        print(coords[n1][0] * coords[n2][0])
        break