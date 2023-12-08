import math;
from functools import reduce

def read_data(test, test_file):
    if test:
        path = f'./test_input{test_file}.txt'
    else:
        path = './input.txt'
    file = open(path, 'r')
    lines = file.readlines()
    
    for i, line in enumerate(lines):
        lines[i] = line.replace('\n', '')
    return lines

def main(test=False, test_file=0):
    lines = read_data(test, test_file)
    
    path = lines[0]
    connections = lines[2:]
    parsed_connections = parse_connections(connections)
    keys = parsed_connections.keys();
    starting_points = [key for key in keys if key[2] == 'A']
    
    loop_distances = []
        
    for start in starting_points:
        distance = follow_path(path, start, parsed_connections)
                 
        loop_distances.append(distance)
        
    loop_lcm = math.lcm(loop_distances[0], loop_distances[1])
    for i in range(2, len(loop_distances)):
        loop_lcm = math.lcm(loop_lcm, loop_distances[i])
    
    return loop_lcm

def parse_connections(connections):
    parsed_connections = {}
    
    for connection in connections:
        split = connection.split("=");
        destinations = split[1].split(',')
        
        parsed_connections[split[0][0:3]] = [destinations[0][2:5], destinations[1][1:4]]
        
    return parsed_connections

def follow_path(path, start, parsed_connections):
    current_loc = start
    current_pos = 0 
    
    initial = True
    while initial or current_loc[2] != "Z":
        initial = False
        direction = 0 if path[current_pos % len(path)] == "L" else 1
        destination = parsed_connections[current_loc][direction]
        
        current_loc = destination
        current_pos += 1

    return current_pos
    
print("Test 1", (main(True, 2) == 6))
print("Ans: ", main())