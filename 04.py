placements = []

with open("04.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()                
        if line:
            row = [False] * len(line)
            for i in range(len(line)):
                if line[i] == "@":
                    row[i] = True
            placements.append(row)

total = 0
first = True
lastRun = -1

while lastRun != 0:
    lastRun = 0
    toBeRemoved = []
    for i in range(len(placements)):
        for j in range(len(placements[i])):
            if not placements[i][j]:
                continue
            top = i > 0
            bottom = i < len(placements)-1
            left = j > 0
            right = j < len(placements[i])-1
            adjacents = 0
            if top:
                adjacents += placements[i-1][j]
                if left:
                    adjacents += placements[i-1][j-1]
                if right:
                    adjacents += placements[i-1][j+1]
            if bottom:
                adjacents += placements[i+1][j]
                if left:
                    adjacents += placements[i+1][j-1]
                if right:
                    adjacents += placements[i+1][j+1]
            if left:
                adjacents += placements[i][j-1]
            if right:
                adjacents += placements[i][j+1]
            if adjacents < 4:
                toBeRemoved.append([i,j])
    lastRun += len(toBeRemoved)
    if first:
        print(lastRun)
        first = False
    total += lastRun
    for r in toBeRemoved:
        placements[r[0]][r[1]] = False
print(total)