#!/usr/bin/env python3

# Output:
# The power consumption of the submarine (part one) is: 3242606.
# The life support rating of the submarine (part two) is: 4856080.


def the_setup():
    the_input = list()
    with open('input_03.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip())

    return the_input


def part_one(the_input):
    output1 = output2 = ''
    for i in range(len(the_input[0])):
        ones = zeroes = 0
        for line in the_input:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeroes += 1

        if ones > zeroes:
            output1 += '1'
            output2 += '0'
        else:
            output1 += '0'
            output2 += '1'

    return int(f"0b{output1}", 2) * int(f"0b{output2}", 2)


def part_two(the_input):
    oxygen_input = the_input[:]
    for i in range(len(oxygen_input[0])):
        ones = zeroes = 0
        for line in oxygen_input:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeroes += 1

        if ones > zeroes:
            for index, line in enumerate(sorted(oxygen_input)):
                if line[i] == '0' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)
        elif zeroes > ones:
            for index, line in enumerate(sorted(oxygen_input)):
                if line[i] == '1' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)
        else:
            for index, line in enumerate(sorted(oxygen_input)):
                if line[i] == '0' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)

    co2_input = the_input[:]
    for i in range(len(the_input[0])):
        ones = zeroes = 0
        for line in co2_input:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeroes += 1

        if ones < zeroes:
            for line in sorted(co2_input):
                if line[i] == '0' and len(co2_input) != 1:
                    co2_input.remove(line)
        elif zeroes < ones:
            for line in sorted(co2_input):
                if line[i] == '1' and len(co2_input) != 1:
                    co2_input.remove(line)
        else:
            for line in sorted(co2_input):
                if line[i] == '1' and len(co2_input) != 1:
                    co2_input.remove(line)

    return int(oxygen_input[0], 2) * int(co2_input[0], 2)


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
    my_input = the_setup()

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    print(f"The power consumption of the submarine (part one) is: {part_one(my_input[:])}.")
    print(f"The life support rating of the submarine (part two) is: {part_two(my_input[:])}.")