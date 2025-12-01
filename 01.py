instructions = []
pos = 50
total1 = 0
total2 = 0

with open("01.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()                
        if line:
            instructions.append(line)

for instruction in instructions:
    oldPos = pos
    oldTotal = total2
    clicks = int(instruction[1:])
    if instruction[:1] == 'L':
        while clicks > 0:
            pos -= 1
            if pos < 0:
                pos += 100
            if pos == 0:
                total2 += 1
            clicks -= 1
    else: 
        while clicks > 0:
            pos += 1
            if pos > 99:
                pos -= 100
            if pos == 0:
                total2 += 1
            clicks -= 1
    if pos == 0:
        total1 += 1

print(total1)
print(total2)