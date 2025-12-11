devices = {}

with open("11.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(':')
            device = parts[0].strip()
            outputs = parts[1].strip().split() if len(parts) > 1 else []
            devices[device] = outputs

def count_paths_with_requirements(start, target, graph, required_devices=None):
    if required_devices is None:
        required_devices = set()
    
    memo = {}
    
    def dfs(current, visited_required):
        state = (current, frozenset(visited_required))
        if state in memo:
            return memo[state]
        if current == target:
            result = 1 if len(visited_required) == len(required_devices) else 0
            memo[state] = result
            return result
        if current not in graph:
            memo[state] = 0
            return 
        total_paths = 0
        for neighbor in graph[current]:
            new_visited = visited_required.copy()
            if neighbor in required_devices:
                new_visited.add(neighbor)
            total_paths += dfs(neighbor, new_visited)
        
        memo[state] = total_paths
        return total_paths
    
    return dfs(start, set())

def count_all_paths(start, target, graph):
    memo = {}
    
    def dfs(current):
        if current in memo:
            return memo[current]
        if current == target:
            return 1
        if current not in graph:
            return 0
        total = sum(dfs(neighbor) for neighbor in graph[current])
        memo[current] = total
        return total
    return dfs(start)

paths_you_count = count_all_paths("you", "out", devices)
print(paths_you_count)

required_devices = {"dac", "fft"}
paths_with_both_count = count_paths_with_requirements("svr", "out", devices, required_devices)
print(paths_with_both_count)
