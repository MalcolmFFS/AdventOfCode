#!/usr/bin/env python3

# Output:
# The bathroom code with a 3x3 number grid (part one) is: 14894.
# The real bathroom code (part two) is: 26B96.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append([c for c in line])

    return the_input


def part_one(the_input: list) -> int:
    bathroom_code = ""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    start_pos = [1, 1]
    for line in the_input:
        for char in line:
            if char == "U" and start_pos[0] > 0: # Up
                start_pos[0] -= 1
            elif char == "R" and start_pos[1] < 2: # Right
                start_pos[1] += 1
            elif char == "L" and start_pos[1] > 0: # Left
                start_pos[1] -= 1
            elif char == "D" and start_pos[0] < 2: # Down
                start_pos[0] += 1

        bathroom_code += str(grid[start_pos[0]][start_pos[1]])

    return bathroom_code


def part_two(the_input: list) -> int:
    bathroom_code = ""
    grid = [
        [" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "],
    ]

    start_pos = [2, 0]
    for line in the_input:
        for char in line:
            try:
                if char == "U" and start_pos[0] > 0 and grid[start_pos[0] - 1][start_pos[1]] != " ":  # Up
                    start_pos[0] -= 1
                elif char == "R" and start_pos[1] < 4 and grid[start_pos[0]][start_pos[1] + 1] != " ": # Right
                    start_pos[1] += 1
                elif char == "L" and start_pos[1] > 0 and grid[start_pos[0]][start_pos[1] - 1] != " ":  # Left
                    start_pos[1] -= 1
                elif char == "D" and start_pos[0] < 4 and grid[start_pos[0] + 1][start_pos[1]] != " ":  # Down
                    start_pos[0] += 1
            except IndexError:
                continue

        bathroom_code += str(grid[start_pos[0]][start_pos[1]])

    return bathroom_code


def main():
    with open('input_02.txt') as f_object:
        input_02 = f_object.read().strip()
    
    # Expected output part 1: 1985
    # Expected output part 2: 5DB3
    sample_input = """ULL
RRDDD
LURDL
UUUUD"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_02)
    
    print(f"The bathroom code with a 3x3 number grid (part one) is: {part_one(my_input)}.")
    print(f"The real bathroom code (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
