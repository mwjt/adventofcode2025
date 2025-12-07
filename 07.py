rows = []

with open("07.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        row = []
        for c in line.strip():
            row.append(c)
        rows.append(row)

startCol = 0
for i in range(len(rows[0])):
    if rows[0][i] == 'S':
        startCol = i
        break

beams = {startCol}

splitCount = 0
for i in range(len(rows)):
    newBeams = set()
    for b in beams:
        if rows[i][b] == '^':
            splitCount+=1
            if b > 0:
                newBeams.add(b-1)
            if b < len(rows[i])-1:
                newBeams.add(b+1)
        else:
            newBeams.add(b)
    beams = newBeams
print(splitCount)

from collections import defaultdict

beams = {startCol}
timelines = {startCol : 1}

for i in range(len(rows)):
    for b in list(beams):
        if rows[i][b] == '^':
            routes_here = timelines[b]
            del timelines[b]
            beams.remove(b)

            if b > 0:
                beams.add(b-1)
                timelines[b-1] = timelines.get(b-1, 0) + routes_here

            if b < len(rows[i]) - 1:
                beams.add(b+1)
                timelines[b+1] = timelines.get(b+1, 0) + routes_here

print(sum(timelines.values()))