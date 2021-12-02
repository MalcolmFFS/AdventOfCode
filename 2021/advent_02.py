#!/usr/bin/env python3

# Output:
# The sub horizontal position times the depth (part one) is: 2039256.
# The sub horizontal position times the depth (part two) is: 1856459736.


def the_setup():
    the_input = list()
    with open('input_02.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input):
    forward = depth = 0
    for line in the_input:
        direction, distance = line.split()
        if direction == 'forward':
            forward += int(distance)
        elif direction == 'down':
            depth += int(distance)
        elif direction == 'up':
            depth -= int(distance)

    return forward * depth


def part_two(the_input):
    forward = depth = aim = 0
    for line in the_input:
        direction, distance = line.split()
        if direction == 'forward':
            forward += int(distance)
            depth += int(distance) * aim
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)

    return forward * depth


sample_input = r"""
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


if __name__ == "__main__":
    my_input = the_setup()

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    print(f"The sub horizontal position times the depth (part one) is: {part_one(my_input)}.")
    print(f"The sub horizontal position times the depth (part two) is: {part_two(my_input)}.")
