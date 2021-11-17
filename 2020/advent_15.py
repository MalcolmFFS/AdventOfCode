#!/usr/bin/env python3


def part_one(the_input, last):
    occurrences = dict()
    last_num = None
    index = 0
    while index < last:
        try:
            i = the_input[index]
            last_num = i
            if i not in occurrences:
                occurrences[i] = list()
            occurrences[i].append(index)
        except IndexError:
            i = last_num
            if len(occurrences[i]) == 1:
                if 0 not in occurrences:
                    occurrences[0] = list()
                occurrences[0].append(index)
                last_num = 0
            else:
                diff = occurrences[i][-1] - occurrences[i][-2]
                if diff not in occurrences:
                    occurrences[diff] = list()
                occurrences[diff].append(index)
                last_num = diff
        index += 1

    return last_num


if __name__ == "__main__":
    my_input = [15, 12, 0, 14, 3, 1]
    print(f"Part one output: {part_one(my_input[:], 2020)}.")
    print(f"Part two output: {part_one(my_input[:], 30000000)}.")
