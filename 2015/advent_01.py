#!/usr/bin/env python3

# Output:
# The floor the instructions take Santa to (part one) is: 232.
# The first position that takes Santa to the basement (part two) is: 1783.

def the_setup(data: str) -> list:
    the_input = list(data)

    return the_input


def part_one(the_input: list) -> int:
    return the_input.count('(') - the_input.count(')')


def part_two(the_input: list) -> int:
    count = 0
    for idx, char in enumerate(the_input, 1):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

        if count == -1:
            break

    return idx


def main():
    with open('input_01.txt') as f_object:
        input_01 = f_object.read().strip()

    # Expected output part 1: -1
    # Expected output part 2: 3
    sample_input = """())"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_01)

    print(f"The floor the instructions take Santa to (part one) is: {part_one(my_input)}.")
    print(f"The first position that takes Santa to the basement (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
