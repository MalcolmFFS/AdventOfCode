#!/usr/bin/env python3

# Output:
# The fuel consumed givin linear fuel cost (part one) is: 355592.
# The fuel consumed given sequential fuel cost (part two) is: 101618069.

# advent_07.py
# part_one():
# real    0m0.031s
# part_two()
# real    0m0.020s


def the_setup() -> list:
    with open('input_07.txt') as f_object:
        for line in f_object:
            the_input = [int(i) for i in line.strip().split(',')]

    return the_input


def part_one(the_input: list) -> int:
    the_input.sort()
    crab_median = the_input[len(the_input) // 2]
    total_fuel = 0
    for crab in the_input:
        increment = 1
        for _ in range(abs(crab - crab_median)):
            total_fuel += increment

    return total_fuel


def part_two(the_input: list) -> int:
    # Eddie Woo's "Sum of an Arithmetic Progression (x of 5: [...])" on YouTube
    # Sum of n terms 1..diff = (n * (1 + len(range(1, diff + 1)) / 2
    # fuel cost will be (distance * (1 + distance)) / 2 # distance for this problem is the same as length n
    # simplified: (distance**2 + distance) / 2
    # diff = abs(crab - position)
    # fuel_cost = (diff * (diff + 1) / 2)

    def calculate_fuel(crabs: list, position: int) -> int:
        total_fuel = 0
        for crab in crabs:
            distance = abs(crab - position)
            total_fuel += (distance**2 + distance) // 2

        return total_fuel

    def find_optimal(crabs: list, starting_point: int) -> int:
        base = calculate_fuel(crabs, starting_point)
        challenger_up = calculate_fuel(crabs, starting_point + 1)
        challenger_down = calculate_fuel(crabs, starting_point - 1)
        if challenger_up < base:
            base = challenger_up
            i = 2
            while calculate_fuel(crabs, starting_point + i) < base:
                base = challenger_up
                i += 1
            return base
        elif challenger_down < base:
            base = challenger_down
            i = 2
            while calculate_fuel(crabs, starting_point - i) < base:
                base = challenger_down
                i += 1
            return base
        else:
            return base

    crab_avg = sum(the_input) // len(the_input)
    fuel = find_optimal(the_input, crab_avg)

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
