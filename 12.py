presents = []
trees = []

present = []
with open("12.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        line = line.split(":")
        if len(line) > 1:
            if len(line[0]) > 1:
                trees.append([line[0], line[1].strip()])
            else:
                if present:
                    presents.append(present)
                    present = []
        else:
            present.append(line[0])
if present:
    presents.append(present)

def parse_shape(shape_lines):
    coords = []
    for r, line in enumerate(shape_lines):
        for c, char in enumerate(line):
            if char == '#':
                coords.append((r, c))
    return coords

def get_rotations_and_flips(coords):
    variations = set()
    for _ in range(4):
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        normalized = tuple(sorted((r - min_r, c - min_c) for r, c in coords))
        variations.add(normalized)
        coords = [(c, -r) for r, c in coords]
    coords = [(r, -c) for r, c in coords]
    for _ in range(4):
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        normalized = tuple(sorted((r - min_r, c - min_c) for r, c in coords))
        variations.add(normalized)
        coords = [(c, -r) for r, c in coords]
    return list(variations)

shape_cache = [get_rotations_and_flips(parse_shape(p)) for p in presents]

def precompute_placements(width, height):
    placements = []
    for shape_idx, variations in enumerate(shape_cache):
        shape_placements = []
        for variation in variations:
            for r in range(height):
                for c in range(width):
                    positions = []
                    valid = True
                    for dr, dc in variation:
                        nr, nc = r + dr, c + dc
                        if nr >= height or nc >= width:
                            valid = False
                            break
                        positions.append(nr * width + nc)
                    if valid:
                        mask = 0
                        for pos in positions:
                            mask |= (1 << pos)
                        shape_placements.append(mask)
        placements.append(shape_placements)
    return placements

def solve_region(width, height, shapes_needed):
    shapes_to_place = []
    for shape_idx, count in enumerate(shapes_needed):
        for _ in range(count):
            shapes_to_place.append(shape_idx)
    
    if not shapes_to_place:
        return True
    
    total_area = sum(len(shape_cache[s][0]) for s in shapes_to_place)
    if total_area > width * height:
        return False
    
    shapes_to_place.sort(key=lambda x: -len(shape_cache[x][0]))
    
    placements = precompute_placements(width, height)
    
    def backtrack(idx, grid):
        if idx == len(shapes_to_place):
            return True
        
        shape_idx = shapes_to_place[idx]
        
        for mask in placements[shape_idx]:
            if not (grid & mask):
                if backtrack(idx + 1, grid | mask):
                    return True
        
        return False
    
    return backtrack(0, 0)

valid_regions = 0
total_trees = len(trees)
for idx, tree_info in enumerate(trees, 1):
    dims, counts = tree_info
    width, height = map(int, dims.split('x'))
    shapes_needed = list(map(int, counts.split()))
    
    print(f"\rProcessing {idx}/{total_trees}", end=" ", flush=True)
    if solve_region(width, height, shapes_needed):
        valid_regions += 1

print(f"\nTotal: {valid_regions}")


