#!/usr/bin/env python3

# Output:
# The elf pairs that have 1 full duplicate (part one) is: 530.
# The elf pairs that overlap at all (part two) is: 903.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        a, b = line.strip().split(',')
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')
        the_input.append(
            [int(a1), int(a2), int(b1), int(b2)]
        )

    return the_input


def part_one(the_input: list) -> int:
    dupe_count = 0

    for a1, a2, b1, b2 in the_input:
        if a1 >= b1 and a2 <= b2:
            dupe_count += 1
        elif b1 >= a1 and b2 <= a2:
            dupe_count += 1
        continue

    return dupe_count


def part_two(the_input: list) -> int:
    overlap_count = 0

    for x in the_input:
        a1, a2, b1, b2 = x
        if a2 in range(b1, b2 + 1):
            overlap_count += 1
        elif b2 in range(a1, a2 + 1):
            overlap_count += 1
        continue

    return overlap_count


def main():
    with open('input_04.txt') as f_object:
        input_04 = f_object.read().strip()

    sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_04)

    print(f"The elf pairs that have 1 full duplicate (part one) is: {part_one(my_input)}.")
    print(f"The elf pairs that overlap at all (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
