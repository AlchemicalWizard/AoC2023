import regex as re


def read_data(test, test_file):
    if test:
        path = f'./test_input{test_file}.txt'
    else:
        path = './input.txt'
    file = open(path, 'r')
    text = file.read()
    
    return text.split('\n')


def main(test=False, test_file=0):
    lines = read_data(test, test_file)

    values = []
    for line in lines:
        values.append(int(calculate_value(line)))

    return sum(values)


def calculate_value(line):
    first = ''
    last = ''
    
    result = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
    first, last = result[0], result[-1]
    
    if not first.isnumeric():
        first = convert_number(first)
        
    if not last.isnumeric():
        last = convert_number(last)
    
    return first + last
    
def convert_number(value):
    match value:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
    
print("Test 1", (main(True, 1) == 281))
print("Ans: ", main())
