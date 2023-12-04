#!/usr/bin/env python3

# Output:
# The checksum of max/min differences (part one) is: 45351.
# The checksum of evenly divisible numbers (part two) is: 275.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append([int(i) for i in line.split()])

    return the_input


def part_one(the_input: list) -> int:
    checksum = 0
    for line in the_input:
        checksum += max(line) - min(line)

    return checksum


def part_two(the_input: list) -> int:
    checksum = 0
    for line in the_input:
        for idx, n in enumerate(line):
            line2 = line[:idx] + line[idx + 1:]
            for n2 in line2:
                if n2 > n:
                    continue

                if n % n2 == 0:
                    checksum += n // n2

    return checksum


def main():
    with open('input_02.txt') as f_object:
        input_02 = f_object.read().strip()
    
    # Expected output part 1: 18
    # Expected output part 2: 32
    sample_input = """5 1 9 5
7 5 3
2 4 6 8"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_02)
    
    print(f"The checksum of max/min differences (part one) is: {part_one(my_input)}.")
    print(f"The checksum of evenly divisible numbers (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
