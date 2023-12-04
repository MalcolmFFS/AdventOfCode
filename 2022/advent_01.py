#!/usr/bin/env python3

# Output:
# The most calories carried by a single elf (part one) is: 71502.
# The top 3 elves together total calories (part two) is: 208191.

def the_setup() -> list:
    # the_input = list()
    with open('input_01.txt') as f_object:
        the_input = f_object.read().split('\n\n')
        the_input = [[int(food) for food in elf.split()] for elf in the_input]
        the_input = [sum(elf) for elf in the_input]

    return the_input


def part_one(the_input):
    return max(the_input)


def part_two(the_input):
    return sum(sorted(the_input)[-3:])


def main():
    sample_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    # To run against sample input
    # my_input = sample_input.split('\n\n')
    # my_input = [[int(food) for food in elf.split()] for elf in my_input]
    # my_input = [sum(elf) for elf in my_input]

    my_input = the_setup()
    print(f"The most calories carried by a single elf (part one) is: {part_one(my_input)}.")
    print(f"The top 3 elves together total calories (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
