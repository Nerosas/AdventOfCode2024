def load_input_file(filename):
    left_list, right_list = [], []

    with open(filename, newline='\n') as input_file:
        for line in input_file:
            line = line.strip()
            line = line.split('   ')
            left_list.append(line[0])
            right_list.append(line[1])

    left_list.sort()
    right_list.sort()
    
    return left_list, right_list


if __name__ == '__main__':
    output = load_input_file('input.txt')