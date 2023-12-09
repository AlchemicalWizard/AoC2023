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
    
    values = []
    for line in lines:
        values.append(int(calculate_value(line)))
    
    return sum(values)

def calculate_value(line):
    first = ''
    last = ''
    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            first = char
            break
    
    for i in range(len(line)-1, -1, -1):
        char = line[i]
        if char.isdigit():
            last = char
            break
    
    return first+last


    
print("Test 1", (main(True, 0) == 142))
print("Ans: ", main())