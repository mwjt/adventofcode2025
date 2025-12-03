joltages = []
total = 0

with open("03.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()                
        if line:
            joltages.append(line)

for joltage in joltages:
    maxL = 0
    for i in range(1,len(joltage)-1):
        if (joltage[i] > joltage[maxL]):
            maxL = i
    maxR = maxL + 1
    for i in range(maxL+1,len(joltage)):
        if (joltage[i] > joltage[maxR]):
            maxR = i
    total += int(joltage[maxL] + joltage[maxR])

print(total)
total = 0
for joltage in joltages:
    maxJoltage = ''
    maxIndex = -1
    for i in range(12):
        maxLocal = maxIndex + 1
        for j in range(maxIndex+1,len(joltage)-11+i):
            if (joltage[j] > joltage[maxLocal]):
                maxLocal = j
        maxJoltage += joltage[maxLocal]
        maxIndex = maxLocal
    total += int(maxJoltage)
print(total)