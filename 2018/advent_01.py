#!/usr/bin/env python3

# Output:
# The resulting frequency after parsing the input (part one) is: 505.
# The first frequency hit a second time from the input (part two) is: 72330.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append(int(line))

    return the_input


def part_one(the_input: list) -> int:
    return sum(the_input)


def part_two(the_input: list) -> int:
    count = 0
    frequency = 0
    frequencies = {0} # Holy hannah this is faster than lists, yay hashmaps
    length = len(the_input)

    while True:
        frequency += the_input[count % length]
        if frequency in frequencies:
            break

        frequencies.add(frequency)
        count += 1

    return frequency


def main():
    with open('input_01.txt') as f_object:
        input_01 = f_object.read().strip()

    # Expected output part 1: 3
    # Expected output part 2: 2
    sample_input = """+1\n-2\n+3\n+1"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_01)

    print(f"The resulting frequency after parsing the input (part one) is: {part_one(my_input)}.")
    print(f"The first frequency hit a second time from the input (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
