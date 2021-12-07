#!/usr/bin/env python3

# Output:
#


def the_setup():
    with open('input_07.txt') as f_object:
        for line in f_object:
            the_input =[int(i) for i in line.strip().split(',')]

    return the_input


def part_one(the_input):
    diffs = dict()
    for i in range(min(the_input), max(the_input) + 1):
        diff = 0
        for crab in the_input:
            diff += abs(crab - i)
        diffs[i] = diff

    optimal_point = min(diffs, key=diffs.get)
    return diffs[optimal_point]


def part_two(the_input):
    diffs = dict()
    for i in range(min(the_input), max(the_input) + 1):
        diff = 0
        for crab in the_input:
            distance = abs(crab - i)
            counter = 0
            for j in range(distance):
                counter += 1
                diff += counter
        print(i)
        diffs[i] = diff

    optimal_point = min(diffs, key=diffs.get)
    return diffs[optimal_point]


def main():
    sample_input = r"""
    16,1,2,0,4,2,7,1,2,14
    """

    # To run against sample input
    # my_input = [int(i) for i in sample_input.strip().split(',')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input[:])}.")
    print(f"The  (part two) is: {part_two(my_input[:])}.")


if __name__ == "__main__":
    main()
