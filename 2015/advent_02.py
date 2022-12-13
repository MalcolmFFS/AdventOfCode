#!/usr/bin/env python3

# Output:
# The total number of square feet of wrapping paper (part one) is: 1586300.
# The total number of feet of ribbon (part two) is: 3737498.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        l, w, h = line.split('x')
        the_input.append([int(l), int(w), int(h)])

    return the_input


def part_one(the_input: list) -> int:
    running_sum = 0

    for present in the_input:
        l, w, h = present
        sides = [l*w, w*h, h*l]

        for side in sides:
            running_sum += 2*side

        running_sum += min(sides) # Slack, smallest side area

    return running_sum


def part_two(the_input: list) -> int:
    running_sum = 0

    for present in the_input:
        l, w, h = present

        running_sum += l*w*h # Volume

        present.remove(max(present))
        small_a, small_b = present
        running_sum += small_a*2 + small_b*2

    return running_sum


def main():
    with open('input_02.txt') as f_object:
        input_02 = f_object.read().strip()
    
    # Expected output part 1: 58
    # Expected output part 2: 34
    sample_input = """2x3x4"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_02)
    
    print(f"The total number of square feet of wrapping paper (part one) is: {part_one(my_input)}.")
    print(f"The total number of feet of ribbon (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
