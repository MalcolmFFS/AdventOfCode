#!/usr/bin/env python3

# Output:
# The captcha solving for numbers that match the next number (part one) is: 1136.
# The captcha solving for numbers that match digit halfway around (part two) is: 1092.

def the_setup(data: str) -> list:
    the_input = [int(i) for i in data]

    return the_input


def part_one(the_input: list) -> int:
    running_sum = 0
    length = len(the_input)
    for idx in range(length):
        if the_input[idx] == the_input[(idx + 1) % length]:
            running_sum += the_input[idx]

    return running_sum


def part_two(the_input: list) -> int:
    running_sum = 0
    length = len(the_input)
    half = length // 2
    for idx in range(length):
        if the_input[idx] == the_input[(idx + half) % length]:
            running_sum += the_input[idx]

    return running_sum


def main():
    with open('input_01.txt') as f_object:
        input_01 = f_object.read().strip()

    # Expected output part 1:
    # Expected output part 2:
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_01)

    print(f"The captcha solving for numbers that match the next number (part one) is: {part_one(my_input)}.")
    print(f"The captcha solving for numbers that match digit halfway around (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
