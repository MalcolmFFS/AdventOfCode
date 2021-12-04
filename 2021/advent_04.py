#!/usr/bin/env python3

# Output:
#


def the_setup():
    the_input = list()
    with open('input_04.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input):
    pass


def part_two(the_input):
    pass


sample_input = r"""
"""


if __name__ == "__main__":
    my_input = the_setup()

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")
