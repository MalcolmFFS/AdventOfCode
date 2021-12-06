#!/usr/bin/env python3

# Output:
# The power consumption of the submarine (part one) is: 3242606.
# The life support rating of the submarine (part two) is: 4856080.


def the_setup() -> list:
    the_input = list()
    with open('input_03.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input: list) -> int:
    gamma = epsilon = ''
    for i in range(len(the_input[0])):
        list_at_index = [j[i] for j in my_input]
        zeroes = list_at_index.count('0')
        ones = list_at_index.count('1')

        if ones > zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def part_two(the_input: list) -> int:
    def find_keepers(thy_input: list, most_common_wins: bool, tie_winner: str) -> int:
        for i in range(len(thy_input[0])):
            list_at_index = [j[i] for j in thy_input]
            zeroes = list_at_index.count('0')
            ones = list_at_index.count('1')
            keepers = thy_input[:]

            if ones > zeroes:
                for line in thy_input:
                    if most_common_wins and line[i] == '0':
                        keepers.remove(line)
                    elif not most_common_wins and line[i] == '1':
                        keepers.remove(line)
                    if len(keepers) == 1:
                        return int(keepers[0], 2)
            elif zeroes > ones:
                for line in thy_input:
                    if most_common_wins and line[i] == '1':
                        keepers.remove(line)
                    elif not most_common_wins and line[i] == '0':
                        keepers.remove(line)
                    if len(keepers) == 1:
                        return int(keepers[0], 2)
            else:
                for line in thy_input:
                    if line[i] != tie_winner:
                        keepers.remove(line)
                    if len(keepers) == 1:
                        return int(keepers[0], 2)

            thy_input = keepers[:]

        return keepers[0]

    oxygen_rating = find_keepers(the_input[:], True, '1')
    co2_rating = find_keepers(the_input[:], False, '0')

    return oxygen_rating * co2_rating


sample_input = r"""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


if __name__ == "__main__":
    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The power consumption of the submarine (part one) is: {part_one(my_input[:])}.")
    print(f"The life support rating of the submarine (part two) is: {part_two(my_input[:])}.")
