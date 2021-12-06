#!/usr/bin/env python3

# The total of times the measurement increased was: 1374.
# The total of times the measurement sum increased was: 1418.


def the_setup() -> list:
    the_input = list()
    with open('input_01.txt') as f_object:
        for line in f_object:
            the_input.append(int(line.strip()))

    return the_input


def part_one(the_input: list) -> int:
    increased_count = 0
    for index, i in enumerate(the_input):
        if index != 0:
            if i > the_input[index - 1]:
                increased_count += 1

    return increased_count


def part_two(the_input: list) -> int:
    measurement_sums = list()
    for index, i in enumerate(the_input):
        try:
            next_one = the_input[index + 1]
            next_two = the_input[index + 2]
            measurement_sums.append(i + next_one + next_two)
        except IndexError:
            break

    increased_count = part_one(measurement_sums)

    return increased_count


sample_input = r"""
199
200
208
210
200
207
240
269
260
263"""


if __name__ == "__main__":
    my_input = the_setup()

    # To run against sample input
    # my_input = [int(i) for i in sample_input.strip().split('\n')]

    print(f"The total of times the measurement increased was: {part_one(my_input)}.")
    print(f"The total of times the measurement sum increased was: {part_two(my_input)}.")
