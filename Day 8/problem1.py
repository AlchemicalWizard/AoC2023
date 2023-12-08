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
    
    start = 'AAA'
    end = 'ZZZ'
    
    distance = follow_path(path, start, end, parsed_connections)
    
    return distance

def parse_connections(connections):
    parsed_connections = {}
    
    for connection in connections:
        split = connection.split("=");
        destinations = split[1].split(',')
        
        parsed_connections[split[0][0:3]] = [destinations[0][2:5], destinations[1][1:4]]
        
    return parsed_connections

def follow_path(path, start, end, parsed_connections):
    current_loc = start
    current_pos = 0
    
    while current_loc != end:
        direction = 0 if path[current_pos % len(path)] == "L" else 1
        destination = parsed_connections[current_loc][direction]
        
        current_loc = destination
        current_pos += 1

    return current_pos
    
print("Test 1", (main(True, 0) == 2))
print("Test 2", (main(True, 1) == 6))
print("Ans: ", main())