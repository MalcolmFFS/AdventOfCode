#!/usr/bin/env python3

# Output:
# The quantity of lanternfish after 80 days (part one) is: 391671.
# The quantity of lanternfish after 256 days (part two) is: 1754000560399.


def the_setup():
    with open('input_06.txt') as f_object:
        for line in f_object:
            the_input = [int(fish) for fish in line.strip().split(',')]

    return the_input


def simulate_lanternfish(the_input, days=80):
    fish_list = list()
    for i in range(0, 9):
        fish_list = [the_input.count(i) if i in the_input else 0 for i in range(9)]

    for day in range(days):
        dupe_fish = fish_list[0]
        new_list = [fish for fish in fish_list[1:]]

        new_list[6] += dupe_fish
        new_list.append(dupe_fish)

        fish_list = new_list[:]

    return sum(fish_list)


def part_one(the_input):
    return simulate_lanternfish(the_input[:], 80)


def part_two(the_input):
    return simulate_lanternfish(the_input[:], 256)


def main():
    sample_input = r"""
    3,4,3,1,2
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The quantity of lanternfish after 80 days (part one) is: {part_one(my_input)}.")
    print(f"The quantity of lanternfish after 256 days (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
