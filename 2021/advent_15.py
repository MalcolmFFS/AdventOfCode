#!/usr/bin/env python3

# Output:
#


def the_setup() -> list:
    with open('input_15.txt') as f_object:
        the_input = [[int(i) for i in line.strip()] for line in f_object.read().split('\n')]

        # tmp = f_object.read().split('\n\n')
        # a = tmp[0]
        # the_input = [int(i) for i in tmp]

    return the_input


def part_one(the_input):
    for r_index, row in enumerate(the_input):
        for c_index, col in enumerate(row):
            


def part_two(the_input):
    pass


def main():
    sample_input = r"""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(my_input)
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
