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

    for i in range(len(left_list)):
        list_of_differences.append(abs(left_list[i] - right_list[i]))

    return sum(list_of_differences)


def calculate_similarity_score(left_list, right_list):
    similarity_score = 0

    for number in left_list:
        number = number * right_list.count(number)
        similarity_score += number

    return similarity_score


if __name__ == '__main__':
    left_list, right_list = load_input_file('input.txt')
    sum_of_differences = add_up_difference_between_two_numbers(left_list, right_list)
    similarity_score = calculate_similarity_score(left_list, right_list)
