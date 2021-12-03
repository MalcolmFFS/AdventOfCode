#!/usr/bin/env python3

# Output:
#


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

    print(output1, output2)

    result = int(f"0b{output1}", 2) * int(f"0b{output2}", 2)

    return result


def part_two(the_input):
    oxygen_input = the_input[:]
    for i in range(len(oxygen_input[0])):
        print(f"Index {i}")
        ones = zeroes = 0
        for line in oxygen_input:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeroes += 1

        if ones > zeroes:
            print(f"Ones beat zeroes, removing zeroes at index {i}.")
            print(oxygen_input, len(oxygen_input))
            for line in sorted(oxygen_input):
                print(line, line[i])
                if line[i] == '0' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)
        elif zeroes > ones:
            print(f"Zeroes beat ones, removing ones at index {i}.")
            for line in sorted(oxygen_input):
                if line[i] == '1' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)
                    print(oxygen_input)
        else:
            print(f"Ones tied zeroes, removing zeroes at index {i}.")
            for line in sorted(oxygen_input):
                if line[i] == '0' and len(oxygen_input) != 1:
                    oxygen_input.remove(line)
                    print(oxygen_input)

    co2_input = the_input[:]
    for i in range(len(the_input[0])):
        print(f"Index {i}")
        ones = zeroes = 0
        for line in co2_input:
            if line[i] == '1':
                ones += 1
            elif line[i] == '0':
                zeroes += 1

        if ones < zeroes:
            print(f"Zeroes beat ones, removing zeroes at index {i}.")
            for line in sorted(co2_input):
                if line[i] == '0' and len(co2_input) != 1:
                    co2_input.remove(line)
        elif zeroes < ones:
            print(f"Ones beat zeroes, removing ones at index {i}.")
            for line in sorted(co2_input):
                if line[i] == '1' and len(co2_input) != 1:
                    co2_input.remove(line)
        else:
            print(f"Ones tied zeroes, removing ones at index {i}.")
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
    # my_input = the_setup()

    # To run against sample input
    my_input = [i for i in sample_input.strip().split('\n')]

    # print(f"The  (part one) is: {part_one(my_input[:])}.")
    print(f"The  (part two) is: {part_two(my_input[:])}.")