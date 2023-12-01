#!/usr/bin/env python3

# Output:
#

def the_setup() -> list:
    with open('input_XX.txt') as f_object:
        my_input = f_object.read().strip()

    the_input = list()
    for line in my_input.split('\n'):
        pass

    return the_input


def part_one(the_input: list) -> int:
    pass


def part_two(the_input: list) -> int:
    pass


def main():
    # Expected output part 1:
    # Expected output part 2:
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_XX)

    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
