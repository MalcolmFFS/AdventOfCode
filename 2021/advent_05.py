#!/usr/bin/env python3

# Output:
#


import re


def the_setup():
    with open('input_05.txt') as f_object:
        tmp_vectors = f_object.read().split('\n')
        the_input = list()
        for vector in tmp_vectors:
            v_start, v_end = re.split(r'->', vector)
            a, b = v_start.strip().split(',')
            start_point = [int(a), int(b)]

            a, b = v_end.strip().split(',')
            end_point = [int(a), int(b)]

            the_input.append([start_point, end_point])

    return the_input


def part_one(the_input):
    counter = dict()
    for start, end in the_input:
        x = 0
        y = 1
        if start[x] == end[x]:
            if start[y] > end[y]:
                first = end[y]
                second = start[y]
            else:
                first = start[y]
                second = end[y]

            for i in range(first, second + 1):
                key = (start[x], i)
                if key not in counter:
                    counter[key] = 0
                counter[key] += 1
            # print(1, counter)
        elif start[y] == end[y]:
            if start[x] > end[x]:
                first = end[x]
                second = start[x]
            else:
                first = start[x]
                second = end[x]

            for i in range(first, second + 1):
                key = (i, start[y])
                if key not in counter:
                    counter[key] = 0
                counter[key] += 1
            # print(2, counter)
        else:
            pass

    count = 0
    for a, b in counter.items():
        if b > 1:
            count += 1

    return count


def part_two(the_input):
    counter = dict()
    for start, end in the_input:
        x = 0
        y = 1
        if start[x] == end[x]:
            if start[y] > end[y]:
                first = end[y]
                second = start[y]
            else:
                first = start[y]
                second = end[y]

            for i in range(first, second + 1):
                key = (start[x], i)
                if key not in counter:
                    counter[key] = 0
                counter[key] += 1
            # print(1, counter)
        elif start[y] == end[y]:
            if start[x] > end[x]:
                first = end[x]
                second = start[x]
            else:
                first = start[x]
                second = end[x]

            for i in range(first, second + 1):
                key = (i, start[y])
                if key not in counter:
                    counter[key] = 0
                counter[key] += 1
            # print(2, counter)
        else:
            if start[y] > end[y] and start[x] > end[x]:
                diff = start[x] - end[x]
                for i in range(diff + 1):
                    key = (end[x] + i, end[y] + i)
                    if key not in counter:
                        counter[key] = 0
                    counter[key] += 1
                # print(2, counter)
            elif start[y] < end[y] and start[x] < end[x]:
                diff = end[x] - start[x]
                for i in range(diff + 1):
                    key = (start[x] + i, start[y] + i)
                    if key not in counter:
                        counter[key] = 0
                    counter[key] += 1
                # print(2, counter)
            else:
                diff = abs(start[x] - end[x])
                if start[x] > end[x]:
                    for i in range(diff + 1):
                        key = (start[x] - i, start[y] + i)
                        if key not in counter:
                            counter[key] = 0
                        counter[key] += 1
                    # print(2, counter)
                else:
                    for i in range(diff + 1):
                        key = (start[x] + i, start[y] - i)
                        if key not in counter:
                            counter[key] = 0
                        counter[key] += 1
                    # print(2, counter)

    count = 0
    for a, b in counter.items():
        if b > 1:
            count += 1

    return count


def main():
    sample_input = r"""
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
