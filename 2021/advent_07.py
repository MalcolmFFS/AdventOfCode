#!/usr/bin/env python3

# Output:
# The fuel consumed givin linear fuel cost (part one) is: 355592.
# The fuel consumed given sequential fuel cost (part two) is: 101618069.

# advent_07.py
# part_one():
# real    0m0.033s
# part_two()
# real    0m57.376s


def the_setup():
    with open('input_07.txt') as f_object:
        for line in f_object:
            the_input = [int(i) for i in line.strip().split(',')]

    return the_input


def calculate_fuel(crabs: list, position: int, base_increment: int = 0) -> int:
    diff = 0
    for crab in crabs:
        increment = 1
        for _ in range(abs(crab - position)):
            diff += increment
            increment += base_increment
    return diff


def part_one(the_input: list) -> int:
    the_input.sort()
    crab_median = the_input[int(len(the_input) / 2)]
    fuel = calculate_fuel(the_input, crab_median)

    return fuel


def part_two(the_input: list) -> int:
    diffs = dict()
    for i in range(min(the_input), max(the_input) + 1):
        diff = 0
        for crab in the_input:
            distance = abs(crab - i)
            counter = 0
            for j in range(distance):
                counter += 1
                diff += counter
        diffs[i] = diff

    optimal_point = min(diffs, key=diffs.get)

    return diffs[optimal_point]

    # ==+==+==+==+==+==+==+==+==+==+==+==+==+==+==

    # I know that this works, but I don't know why it works, whereas I do know why median works for pt1

    # input_avg = int(sum(the_input) / len(the_input))
    # fuel = calculate_fuel(the_input, input_avg, 1)

    # Supposedly, this is even better, but I also wouldn't even be able to consider turning this into an equation
    # units = int(abs(crab - position))
    # fuel = int(units * units / 2 + units / 2)
    # return fuel

    # return fuel


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
