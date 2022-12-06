#!/usr/bin/env python3

from collections import deque

# Output:
# The first start-of-packet marker ends (part one) at: 1987.
# The first start-of-message ends (part two) at: 3059.

def the_setup(data: str) -> list:
    the_input = list(data)

    return the_input


def part_one(the_input: list) -> int:
    the_queue = deque(maxlen=4)

    for idx, c in enumerate(the_input):
        if len(the_queue) < 4:
            the_queue.append(c)
        else:
            if len(set(the_queue)) == len(the_queue):
                return idx
            the_queue.append(c)


def part_two(the_input: list) -> int:
    the_queue = deque(maxlen=14)

    for idx, c in enumerate(the_input):
        if len(the_queue) < 14:
            the_queue.append(c)
        else:
            if len(set(the_queue)) == len(the_queue):
                return idx
            the_queue.append(c)


def main():
    with open('input_06.txt') as f_object:
        input_06 = f_object.read().strip()

    # Expected output part 1: 7
    # Expected output part 2: 19
    sample_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_06)
    
    print(f"The first start-of-packet marker ends (part one) at: {part_one(my_input)}.")
    print(f"The first start-of-message ends (part two) at: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
