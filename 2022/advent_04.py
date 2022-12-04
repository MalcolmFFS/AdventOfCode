#!/usr/bin/env python3

# Output:
#

def the_setup() -> list:
    the_input = list()
    with open('input_04.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip().split(','))

        # tmp = f_object.read().split('\n\n')
        # a = tmp[0]
        # the_input = [int(i) for i in tmp]

    return the_input


def part_one(the_input: list) -> int:
    dupe_count = 0

    for a, b in the_input:
        a_min, a_max = a.split('-')
        b_min, b_max = b.split('-')
        print(f"A: {a_min}, {a_max}; B: {b_min}, {b_max}")
        if a_min >= b_min and a_max <= b_max:
            dupe_count += 1
        elif b_min >= a_min and b_max <= a_max:
            dupe_count += 1

        print(dupe_count)
        continue

    return dupe_count


def part_two(the_input: list) -> int:
    pass


def main():
    sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    # To run against sample input
    # my_input = [i.split(',') for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
