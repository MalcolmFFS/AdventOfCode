#!/usr/bin/env python3

# Output:
# 

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        pass

    return the_input


def part_one(the_input: list) -> int:
    pass


def part_two(the_input: list) -> int:
    pass


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
    
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
