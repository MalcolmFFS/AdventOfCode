#!/usr/bin/env python3

# Output:
# The total explosions after 100 steps (part one) is: 1652.
# The total steps until all explode at once (part two) is: 220.

# advent_11.py
# part_one():
# real    0m0.043s
# part_two()
# real    0m0.030s


def the_setup() -> list:
    with open('input_11.txt') as f_object:
        the_input = [[int(i) for i in line.strip()] for line in f_object.read().split('\n')]

    return the_input


def explode(the_input, point):
    explosions = 1
    not_top_row = point[0] != 0
    not_right_col = point[1] != len(the_input[point[0]]) - 1
    not_bottom_row = point[0] != len(the_input) - 1
    not_left_col = point[1] != 0
    if not_top_row:  # up
        the_input[point[0] - 1][point[1]] += 1
        if the_input[point[0] - 1][point[1]] == 10:
            explosions += explode(the_input, (point[0] - 1, point[1]))

        if not_right_col:  # up+right diag
            the_input[point[0] - 1][point[1] + 1] += 1
            if the_input[point[0] - 1][point[1] + 1] == 10:
                explosions += explode(the_input, (point[0] - 1, point[1] + 1))

        if not_left_col:  # up+left diag
            the_input[point[0] - 1][point[1] - 1] += 1
            if the_input[point[0] - 1][point[1] - 1] == 10:
                explosions += explode(the_input, (point[0] - 1, point[1] - 1))

    if not_right_col:  # right
        the_input[point[0]][point[1] + 1] += 1
        if the_input[point[0]][point[1] + 1] == 10:
            explosions += explode(the_input, (point[0], point[1] + 1))

    if not_bottom_row:  # down
        the_input[point[0] + 1][point[1]] += 1
        if the_input[point[0] + 1][point[1]] == 10:
            explosions += explode(the_input, (point[0] + 1, point[1]))

        if not_right_col:  # up+right diag
            the_input[point[0] + 1][point[1] + 1] += 1
            if the_input[point[0] + 1][point[1] + 1] == 10:
                explosions += explode(the_input, (point[0] + 1, point[1] + 1))

        if not_left_col:  # up+left diag
            the_input[point[0] + 1][point[1] - 1] += 1
            if the_input[point[0] + 1][point[1] - 1] == 10:
                explosions += explode(the_input, (point[0] + 1, point[1] - 1))

    if not_left_col:  # left
        the_input[point[0]][point[1] - 1] += 1
        if the_input[point[0]][point[1] - 1] == 10:
            explosions += explode(the_input, (point[0], point[1] - 1))

    return explosions


def part_one(the_input):
    total_explosions = 0
    copy_input = [[c for c in line] for line in the_input]
    for _ in range(100):
        for r_index, row in enumerate(copy_input):
            for c_index, col in enumerate(row):
                copy_input[r_index][c_index] += 1
                if copy_input[r_index][c_index] == 10:
                    total_explosions += explode(copy_input[:], (r_index, c_index))

        for r_index, row in enumerate(copy_input):
            for c_index, col in enumerate(row):
                if copy_input[r_index][c_index] > 9:
                    copy_input[r_index][c_index] = 0

    return total_explosions


def part_two(the_input):
    counter = 0
    while True:
        counter += 1
        for r_index, row in enumerate(the_input):
            for c_index, col in enumerate(row):
                the_input[r_index][c_index] += 1
                if the_input[r_index][c_index] == 10:
                    _ = explode(the_input[:], (r_index, c_index))

        for row in the_input:
            row_len = len([octopus for octopus in row if octopus < 10])
            if row_len != 0:
                break
            else:
                continue
        else:
            return counter

        for r_index, row in enumerate(the_input):
            for c_index, col in enumerate(row):
                if the_input[r_index][c_index] > 9:
                    the_input[r_index][c_index] = 0


def main():
    sample_input = r"""
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    """

    # To run against sample input
    # my_input = [[int(i) for i in line.strip()] for line in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The total explosions after 100 steps (part one) is: {part_one(my_input[:])}.")
    print(f"The total steps until all explode at once (part two) is: {part_two(my_input[:])}.")


if __name__ == "__main__":
    main()
