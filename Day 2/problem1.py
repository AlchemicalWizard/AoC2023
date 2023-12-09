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
    possible_games = []
    for i, line in enumerate(lines):
        possible = parse_values(line, limit_r, limit_g, limit_b)
        if possible:
            possible_games.append(i+1)
    return sum(possible_games)

    
def parse_values(line, r_limit, g_limit, b_limit):
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
        if red > r_limit or blue > b_limit or green > g_limit:
            return False
    return True
    
    
    
print("Test 1", (main(True, 0) == 8))
print("Ans: ", main())