#!/usr/bin/env python3

from collections import Counter
from itertools import combinations

# Output:
# The checksum of boxes matching twos and threes (part one) is: 7688.
# The common letters for the correct boxes (part two) is: lsrivmotzbdxpkxnaqmuwcchj.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append(list(line))

    return the_input


def part_one(the_input: list) -> int:
    twos = 0
    threes = 0
    for line in the_input:
        counts = Counter(line)
        for k, v in counts.items():
            if v == 2:
                twos += 1
                break

        for k, v in counts.items():
            if v == 3:
                threes += 1
                break

    return twos * threes


def part_two(the_input: list) -> str:
    mixed = combinations(the_input, 2)

    for a, b in mixed:
        errors = 0
        output = str()
        for idx, char in enumerate(a):
            if char == b[idx]:
                output += char
            else:
                errors += 1
                if errors > 1:
                    break
        else:
            return output


def main():
    with open('input_02.txt') as f_object:
        input_02 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_02)
    
    print(f"The checksum of boxes matching twos and threes (part one) is: {part_one(my_input)}.")
    print(f"The common letters for the correct boxes (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
