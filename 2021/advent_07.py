#!/usr/bin/env python3

# Output:
#


def the_setup():
    with open('input_07.txt') as f_object:
        for line in f_object:
            the_input = [int(i) for i in line.strip().split(',')]

    return the_input


def calculate_fuel(crabs, position, base_increment=0):
    diff = 0
    for crab in crabs:
        increment = 1
        for _ in range(abs(crab - position)):
            diff += increment
            increment += base_increment
    return diff


def part_one(the_input):
    the_input.sort()
    crab_median = the_input[int(len(the_input) / 2)]
    fuel = calculate_fuel(the_input, crab_median)

    return fuel


def part_two(the_input):
    input_avg = int(sum(the_input) / len(the_input))
    fuel = calculate_fuel(the_input, input_avg, 1)

    return fuel


def main():
    sample_input = r"""
    16,1,2,0,4,2,7,1,2,14
    """

    # To run against sample input
    # my_input = [int(i) for i in sample_input.strip().split(',')]

    my_input = the_setup()
    print(f"The fuel consumed givin linear fuel cost (part one) is: {part_one(my_input[:])}.")
    print(f"The fuel consumed given sequential fuel cost (part two) is: {part_two(my_input[:])}.")


if __name__ == "__main__":
    main()
