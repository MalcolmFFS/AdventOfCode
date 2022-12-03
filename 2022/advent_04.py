#!/usr/bin/env python3

# Output:
#

def the_setup() -> list:
    the_input = list()
    with open('input_04.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

        # tmp = f_object.read().split('\n\n')
        # a = tmp[0]
        # the_input = [int(i) for i in tmp]

    return the_input


def part_one(the_input: list) -> int:
    pass


def part_two(the_input: list) -> int:
    pass


def main():
    sample_input = """
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
