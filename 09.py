
from itertools import combinations

reds = []

with open("09.txt", 'r') as file:
    for line in file:
        line = line.strip().split(',')
        reds.append((int(line[0]), int(line[1])))

def area(pos1, pos2):
    return (abs(pos1[0] - pos2[0]) + 1) * (abs(pos1[1] - pos2[1]) + 1)

max_area = max(
    area(p1, p2)
    for p1, p2 in combinations(reds, 2)
)
print(max_area)

columns = {}  
rows = {}    

def get_tiles():
    data_loop = reds + [reds[0]]  
    for i in range(len(data_loop) - 1):
        t1, t2 = data_loop[i], data_loop[i + 1]
        if t1[0] == t2[0]: 
            x = t1[0]
            y_range = range(min(t1[1], t2[1]), max(t1[1], t2[1]) + 1)
            if x not in columns:
                columns[x] = []
            columns[x].append(y_range)
        else:  
            y = t1[1]
            x_range = range(min(t1[0], t2[0]), max(t1[0], t2[0]) + 1)
            if y not in rows:
                rows[y] = []
            rows[y].append(x_range)

def rg_area(pos1, pos2):
    opposite1 = (pos1[0], pos2[1])
    opposite2 = (pos2[0], pos1[1])
    
    for opposite in (opposite1, opposite2):
        if opposite in reds:  
            continue
            
        x, y = opposite
        top, right, left, bottom = 0, 0, 0, 0
        
        for ry, yrows in rows.items():
            if ry == y:  
                if any((x in row for row in yrows)):
                    break  
                right -= 2 * len([row for row in yrows if row[0] > x])
                left -= 2 * len([row for row in yrows if row[-1] < x])
            elif ry < y:  
                if any((x in row for row in yrows)):
                    top += 1
            else:  
                if any((x in row for row in yrows)):
                    bottom += 1
        else:
            for cx, xcols in columns.items():
                if cx == x: 
                    if any((y in col for col in xcols)):
                        break  
                    top -= 2 * len([col for col in xcols if col[-1] < y])
                    bottom -= 2 * len([col for col in xcols if col[0] > y])
                elif cx < x: 
                    if any((y in col for col in xcols)):
                        left += 1
                else:  
                    if any((y in col for col in xcols)):
                        right += 1
            else:
                
                if not (top % 2 and bottom % 2) and not (right % 2 and left % 2):
                    return 0  
    
    corners = [pos1, opposite1, pos2, opposite2]
    for i in range(4):
        c1, c2 = corners[i], corners[(i + 1) % 4]
        if c1[0] == c2[0]:  
            for y in range(min(c1[1], c2[1]) + 1, max(c1[1], c2[1])):
                if any((c1[0] in row for row in rows.get(y, []))):
                    return 0
        else:  
            for x in range(min(c1[0], c2[0]) + 1, max(c1[0], c2[0])):
                if any((c1[1] in column for column in columns.get(x, []))):
                    return 0
    
    return area(pos1, pos2)

get_tiles()

max_area = max(
    rg_area(p1, p2)
    for p1, p2 in combinations(reds, 2)
)

print(max_area)