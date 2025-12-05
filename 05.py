first_part = True
ranges = []
total = 0

with open("05.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        if line == "\n":
            first_part = False
        line = line.strip()                
        if line:
            if first_part:
                ranges.append([int(line.split("-")[0]), int(line.split("-")[1])])
            else:
                ingredient = int(line)
                for r in ranges:
                    # print(str(r[0]) + "-" + str(r[1]) + "   -    " + str(ingredient))
                    if ingredient >= r[0] and ingredient <= r[1]:
                        total += 1
                        break

print(total)
total = 0
changes = True
while changes:
    changes = False
    for i in range(len(ranges)):
        for j in range(len(ranges)):
            if i == j:
                continue
            left = ranges[j][0] >= ranges[i][0] and ranges[j][0] <= ranges[i][1]
            right = ranges[j][1] >= ranges[i][0] and ranges[j][1] <= ranges[i][1]

            if left and not right:
                ranges[i][1] = ranges[j][1]
                ranges[j] = [0,0]
                changes = True
            elif not left and right:
                ranges[i][0] = ranges[j][0]
                ranges[j] = [0,0]
                changes = True
            if left and right:
                ranges[j] = [0,0]

total = 0
for r in ranges:
    if r != [0,0]:
        total += r[1] - r[0] + 1

print(total)