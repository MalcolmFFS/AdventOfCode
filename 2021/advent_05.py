#!/usr/bin/env python3

# Output:
# There are smoke lines without diagonals overlap 2+ times (part one) 7438 times.
# There are smoke lines with diagonals overlaping 2+ times (part one) 21406 times.

# advent_05.py
# part_one():
# real    0m0.062s
# part_two()
# real    0m0.093s


import re
from collections import defaultdict


def the_setup() -> list:
    with open('input_05.txt') as f_object:
        tmp_vectors = f_object.read().split('\n')
        the_input = list()
        for vector in tmp_vectors:
            groups = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", vector)
            ax, ay = int(groups[1]), int(groups[2])
            bx, by = int(groups[3]), int(groups[4])
            the_input.append([[ax, ay], [bx, by]])

    return the_input


def check_all_lines(the_input: list, diagonals: bool = False) -> int:
    def find_step(a: list, b: list) -> tuple:
        if a[0] > b[0]:
            xstep = -1
        elif a[0] < b[0]:
            xstep = 1
        else:
            xstep = 0

        if a[1] > b[1]:
            ystep = -1
        elif a[1] < b[1]:
            ystep = 1
        else:
            ystep = 0

        return xstep, ystep

    def find_diff(a: list, b: list) -> int:
        xdiff, ydiff = abs(a[0] - b[0]), abs(a[1] - b[1])
        if xdiff == ydiff:
            return xdiff
        else:
            return abs(xdiff - ydiff)

    def find_count_of_repetitions(the_counter: dict, repetitions: int = 2) -> int:
        return len([a for a in the_counter.values() if a >= repetitions])

    counter = defaultdict(int)
    x = 0
    y = 1
    for start, end in the_input:
        step_x, step_y = find_step(start, end)
        diff = find_diff(start, end)

        if step_x != 0 and step_y != 0 and diagonals is False:
            continue

        x_coord = start[x]
        y_coord = start[y]
        for i in range(diff + 1):
            key = (x_coord, y_coord)
            counter[key] += 1
            x_coord += step_x
            y_coord += step_y

    return find_count_of_repetitions(counter)


def part_one(the_input: list) -> int:
    return check_all_lines(the_input)


def part_two(the_input: list) -> int:
    return check_all_lines(the_input, True)


def main():
    my_input = the_setup()
    print(f"The overlaps of at least 2 smoke lines without diagonals (part one) is: {part_one(my_input)}.")
    print(f"The overlaps of at least 2 smoke lines with diagonals (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
