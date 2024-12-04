def load_input_file(filename):
    left_list, right_list = [], []

    with open(filename, newline='\n') as input_file:
        for line in input_file:
            line = line.strip().split('   ')
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))

    left_list.sort()
    right_list.sort()
    
    return left_list, right_list


def add_up_difference_between_two_numbers(left_list, right_list):
    list_of_differences = []

    for i in range(0, len(left_list)-1):
        list_of_differences.append(abs(left_list[i] - right_list[i]))

    return sum(list_of_differences)


if __name__ == '__main__':
    list_1, list_2 = load_input_file('input.txt')
    answer = add_up_difference_between_two_numbers(list_1, list_2)
    print(answer)
