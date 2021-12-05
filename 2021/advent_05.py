#!/usr/bin/env python3

# Output:
# There are smoke lines without diagonals overlap 2+ times (part one) 7438 times.
# There are smoke lines with diagonals overlaping 2+ times (part one) 21406 times.


from collections import defaultdict


def the_setup():
    with open('input_05.txt') as f_object:
        tmp_vectors = f_object.read().split('\n')
        the_input = list()
        for vector in tmp_vectors:
            v_start, v_end = vector.split(' -> ')
            a, b = v_start.strip().split(',')
            start_point = [int(a), int(b)]

            a, b = v_end.strip().split(',')
            end_point = [int(a), int(b)]

            the_input.append([start_point, end_point])

    return the_input


def check_all_lines(the_input, diagonals=False):
    def find_step(a, b):
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

    def find_diff(a, b):
        xdiff, ydiff = abs(a[0] - b[0]), abs(a[1] - b[1])
        if xdiff == ydiff:
            return xdiff
        else:
            return abs(xdiff - ydiff)

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

    return counter


def part_one(the_input):
    counter = check_all_lines(the_input)

    count = 0
    for a, b in counter.items():
        if b > 1:
            count += 1

    return count


def part_two(the_input):
    counter = check_all_lines(the_input, True)

    count = 0
    for a, b in counter.items():
        if b > 1:
            count += 1

    return count


def main():
    my_input = the_setup()
    print(f"The overlaps of at least 2 smoke lines without diagonals (part one) is: {part_one(my_input)}.")
    print(f"The overlaps of at least 2 smoke lines with diagonals (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
