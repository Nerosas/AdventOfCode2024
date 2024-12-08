import re

def load_input_file(filename):
    memory = ""

    with open(filename) as input_file:
        memory = input_file.read()
    
    return memory


def find_uncorrupted_commands(memory):
    pattern_matching = re.compile(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)")
    valid_commands = pattern_matching.findall(memory)

    return valid_commands


def execute_mul_command(valid_command):
    pattern_matching = re.compile(r'\d{1,3}')
    numbers = pattern_matching.findall(valid_command)
    result = int(numbers[0]) * int(numbers[1])

    return result


def add_up_results(valid_commands):
    total = 0
    do = True
    for command in valid_commands:
        if command == "do()":
            do = True
        elif command == "don't()":
            do = False
        elif do:
            result = execute_mul_command(command)
            total += result

    return total


if __name__ == "__main__":
    memory = load_input_file("input.txt")
    valid_commands = find_uncorrupted_commands(memory)
    print(add_up_results(valid_commands))