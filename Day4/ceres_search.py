def load_input_file(filename):
    input = []

    with open(filename) as input_file:
        input = input_file.readlines()

    
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        input[i] = list(input[i])

    return input


def count_xmas_occurrences(wordsearch):
    count = 0

    for i in range(1, len(wordsearch) - 1):
        for j in range(1, len(wordsearch[i]) - 1):
            if wordsearch[i][j] == 'A':
                if ((wordsearch[i-1][j-1] == 'M' and wordsearch[i+1][j+1] == 'S') or (wordsearch[i-1][j-1] == 'S' and wordsearch[i+1][j+1] == 'M')) and ((wordsearch[i-1][j+1] == 'M' and wordsearch[i+1][j-1] == 'S') or (wordsearch[i-1][j+1] == 'S' and wordsearch[i+1][j-1] == 'M')):
                    count += 1

    return count


if __name__ == '__main__':
    grid = load_input_file("input.txt")
    occurrences = count_xmas_occurrences(grid)

    print(occurrences)