#!/usr/bin/env python3

import string

# Output:
#

def the_setup() -> list:
    the_input = list()
    with open('input_03.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input):
    shared_types = str()

    for rucksack in the_input:
        half = len(rucksack)//2
        pocket_1, pocket_2 = rucksack[:half], rucksack[half:]
        for item in pocket_1:
            if item in pocket_2:
                shared_types += item
                break

    print(shared_types)
    item_values = dict()
    for value, char in enumerate(string.ascii_letters, 1):
        item_values[char] = value

    total = 0
    for char in shared_types:
        total += item_values[char]

    return total


def part_two(the_input):
    groups = [the_input[i:i+3] for i in range(len(the_input)) if i % 3 == 0]

    uniques = str()

    for group in groups:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                uniques += char
                break

    item_values = dict()
    for value, char in enumerate(string.ascii_letters, 1):
        item_values[char] = value

    print(uniques)
    total = 0
    for char in uniques:
        total += item_values[char]

    return total


def main():
    sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
