rows = []
with open("06.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line.strip()
        row = []
        lineChars = line.split()
        if lineChars[0] == "*" or lineChars[0] == "+":
            for i in lineChars:
                row.append(i)
        else:
            for i in line.split():
                row.append(int(i)) 
        rows.append(row)

total = 0
for col in range(len(rows[0])):
    op = rows[len(rows)-1][col]
    if op == "+":
        res = 0
        for i in range(len(rows)-1):
            res += rows[i][col]
    elif op == "*":
        res = 1
        for i in range(len(rows)-1):
            res *= rows[i][col]
    total += res
print(total)

rows = []
with open("06.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        rows.append(line.replace("\n",""))

left = len(rows[0])-2
right = left+1
total = 0
while left >= 0:
    if rows[len(rows)-1][left] not in ('+','*'):
        left -= 1
        continue
    col = []
    
    for i in range(right,left-1,-1):
        entry = ""
        for j in range(len(rows)-1):
            entry += rows[j][i]
        col.append(int(entry))

    if rows[len(rows)-1][left] == '+' :
        res = 0
        for i in col:
            res += i
    else:
        res = 1
        for i in col:
            res *= i
    total += res 

    left -= 1
    found = False
    while left >= 0:
        for i in range(len(rows)-1):
            if rows[i][left] != " ":
                found = True
                break
        if found:
            break
        left -= 1
    right = left
    left -= 1
print(total)