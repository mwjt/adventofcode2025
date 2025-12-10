from collections import deque
from z3 import *

machines = []

with open("10.txt", 'r') as file:
    for line in file:
        machine = {}
        line = line.strip().split()
        machine['lights'] = line[0][1:-1]
        machine['buttons'] = []
        for i in range(1,len(line)-1):
            buttons = []
            for button in line[i][1:-1].split(','):
                buttons.append(int(button))
            machine['buttons'].append(buttons)
        joltages = []
        for joltage in line[-1][1:-1].split(','):
            joltages.append(int(joltage)) 
        machine['joltage'] = joltages
        machines.append(machine)

def solve_joltage_machine_z3(machine):
    target = machine['joltage']
    buttons = machine['buttons']
    n_counters = len(target)
    n_buttons = len(buttons)
    
    opt = Optimize()
    
    button_presses = [Int(f'button_{i}') for i in range(n_buttons)]
    
    for var in button_presses:
        opt.add(var >= 0)
    
    for counter_idx in range(n_counters):
        counter_sum = 0
        for button_idx, button in enumerate(buttons):
            if counter_idx in button:
                counter_sum += button_presses[button_idx]
        opt.add(counter_sum == target[counter_idx])
    
    total_presses = Sum(button_presses)
    opt.minimize(total_presses)
    
    if opt.check() == sat:
        model = opt.model()
        return model.eval(total_presses).as_long()
    else:
        return None

def solve_lights_machine_bfs(machine):
    target = machine['lights']
    buttons = machine['buttons']
    n_lights = len(target)
    
    target_state = tuple(c == '#' for c in target)
    initial_state = tuple(False for _ in range(n_lights))
    
    if initial_state == target_state:
        return 0
    
    queue = deque([(initial_state, 0)])
    visited = {initial_state}
    
    while queue:
        current_state, presses = queue.popleft()
        
        for button in buttons:
            new_state = list(current_state)
            for light_idx in button:
                if light_idx < n_lights:
                    new_state[light_idx] = not new_state[light_idx]
            
            new_state = tuple(new_state)
            
            if new_state == target_state:
                return presses + 1
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))
    
    return None

total = 0
for i, machine in enumerate(machines):
    result = solve_lights_machine_bfs(machine)
    if result is not None:
        total += result
print(total)

total = 0
for i, machine in enumerate(machines):
    result = solve_joltage_machine_z3(machine)
    if result is not None:
        total += result
print(total)