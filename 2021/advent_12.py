#!/usr/bin/env python3

# Output:
#


from collections import defaultdict


def the_setup() -> list:
    with open('input_12.txt') as f_object:
        the_input = [i.strip() for i in f_object.read().strip().split('\n')]

    for index, step in enumerate(the_input):
        a, b = step.split('-')
        if 'start' in b:
            the_input[index] = [b, a]
        elif 'end' in a:
            the_input[index] = (b, a)
        else:
            the_input[index] = (a, b)

    return the_input


def part_one(the_input):
    starters = list()
    enders = list()
    for step in the_input:
        a, b = step
        if a == 'start':
            starters.append(step)
        elif b == 'end':
            enders.append(step)

    steps = defaultdict(list)
    for step in the_input:
        a, b = step
        steps[a].append(b)

    paths =
    for step in steps:
        a, b = step
        pass


def part_two(the_input):
    pass


def find_path(steps):
    paths = list
    for key, values in steps.items():
        if key[0] == 'start':
            path = [key[0], key[1]]



def main():
    sample_input = r"""
    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end
    """

    # To run against sample input
    my_input = [tuple(i.strip().split('-')) for i in sample_input.strip().split('\n')]

    # my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
