def is_pattern(num):
    s = str(num)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        pattern = s[:pattern_len]
        
        if pattern * (length // pattern_len) == s and length % pattern_len == 0:
            if length // pattern_len >= 2:
                return True
    
    return False

ranges = []
total = 0

with open("02.txt", 'r') as file:
    for line_number, line in enumerate(file, 1):
        line = line.strip()                
        if line:
            range_pairs = line.split(',')
            for range_pair in range_pairs:
                low, high = range_pair.split('-')
                ranges.append(range(int(low), int(high)+1))

for r in ranges:
    for i in r:
        if is_pattern(i):
            total += i

print(total)