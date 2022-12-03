#!/usr/bin/env python3

import string

# Output:
# The priority of items in both pockets (part one) is: 8298.
# The priority of group badges (part two) is: 2708.

def the_setup() -> list:
    the_input = list()
    with open('input_03.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input: list, priority: dict) -> int:
    shared_types = str()

    for rucksack in the_input:
        half = len(rucksack)//2
        pocket_1, pocket_2 = rucksack[:half], rucksack[half:]
        for item in pocket_1:
            if item in pocket_2:
                shared_types += item
                break

    return sum([priority[i] for i in shared_types])


def part_two(the_input: list, priority: dict) -> int:
    uniques = str()

    groups = [the_input[i:i+3] for i in range(len(the_input)) if i % 3 == 0]
    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                uniques += char
                break

    return sum([priority[i] for i in uniques])


def main():
    sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    item_values = {v: k for k, v in enumerate(string.ascii_letters, 1)}

    my_input = the_setup()
    print(f"The priority of items in both pockets (part one) is: {part_one(my_input, item_values)}.")
    print(f"The priority of group badges (part two) is: {part_two(my_input, item_values)}.")


if __name__ == "__main__":
    main()
