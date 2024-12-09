def load_input_file(filename):
    input = []

    with open(filename) as input_file:
        input = input_file.readlines()

    
    for i in range(len(input)):
        input[i] = input[i].rstrip()

    return input


def search_horizontal(line):
    count = 0

    for i in range(len(line)):
        if i < len(line) - 4:
            if line[i:i+4] == ("XMAS" or "SAMX"):
                count += 1

    return count


def search_vertical(input):
    count = 0

    for i in range(len(input)-4):
        for j in range(len(input[i])):
            string_builder = ''

            for k in range(4):
                string_builder += input[i+k][j]

            if string_builder == ("XMAS" or "SAMX"):
                count += 1
    
    return count


def search_diagonal(input):
    count = 0

    #search in south-east and north-west direction
    for i in range(len(input)-4):
        for j in range(len(input)-4):
            string_builder = ''

            for k in range(4):
                string_builder += input[i+k][j+k]

            if string_builder == ("XMAS" or "SAMX"):
                count += 1

    #search in south-west and north-east direction
    for i in range(len(input)-4):
        for j in range(len(input)-4):
            string_builder = ''

            for k in range(4):
                string_builder += input[i+k][j-k]

            if string_builder == ("XMAS" or "SAMX"):
                count += 1

    return count



if __name__ == "__main__":
    wordsearch = load_input_file("input.txt")
    count = 0

    for line in wordsearch:
        count += search_horizontal(line)

    count += search_vertical(wordsearch)
    count += search_diagonal(wordsearch)

    print(count)