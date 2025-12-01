instructions = []
pos = 50
total = 0

with open("01.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()                
        if line:
            instructions.append(line)

for instruction in instructions:
    clicks = int(instruction[1:]) % 100
    if instruction[:1] == 'L':
        pos -= clicks
        if pos < 0:
            pos += 100
    else:
        pos += clicks
        if pos > 99:
            pos -= 100
    if pos == 0:
        total += 1

print(total)