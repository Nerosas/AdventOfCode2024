def load_input_file(filename):
    input = []

    with open(filename) as input_file:
        input = input_file.readlines()

    
    for i in range(len(input)):
        input[i] = input[i].rstrip()
        input[i] = list(input[i])

    return input


def count_four_letter_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    # Helper function to check a word in a given direction
    def check_word(x, y, dx, dy):
        for i in range(4):
            new_x = x + i * dx
            new_y = y + i * dy
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or grid[new_x][new_y] != word[i]:
                return False
        return True

    # Variable to count occurrences of the word
    word_count = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # For each direction: right, left, down, up, diagonal right-down, diagonal left-down, diagonal right-up, diagonal left-up
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    word_count += 1

    return word_count


if __name__ == '__main__':
    grid = load_input_file("input.txt")

    word = 'XMAS'

    occurrences = count_four_letter_word_occurrences(grid, word)

    if occurrences > 0:
        print(f"Word '{word}' found {occurrences} time(s).")
    else:
        print(f"Word '{word}' not found.")
