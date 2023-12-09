import regex

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
    
    limit_r, limit_g, limit_b = 12, 13, 14
    powers = []
    for i, line in enumerate(lines):
        power = parse_values(line)
        powers.append(power)
    return sum(powers)

    
def parse_values(line):
    max_blue, max_green, max_red = 0, 0 , 0
    
    rounds = line.split(':')[1].split(';')
    for single_round in rounds:
        scores = single_round.split(',')
        blue = 0
        green = 0
        red = 0
        for score in scores:
            colour = regex.findall('red|blue|green', score)
            
            match colour[0]:
                case 'red':
                    red += int(score.split(' red')[0])
                case 'green':
                    green += int(score.split(' green')[0])
                case 'blue':
                    blue += int(score.split(' blue')[0])
            
        if red > max_red: max_red = red
        if green > max_green: max_green = green
        if blue > max_blue: max_blue = blue
        
    return max_blue * max_red * max_green
    
    
print("Test 1", (main(True, 0) == 2286))
print("Ans: ", main())