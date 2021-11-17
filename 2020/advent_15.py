#!/usr/bin/env python3


def part_one(the_input):
    occurrences = dict()
    full_list = list()
    index = 0
    while index < 2020:
        try:
            i = the_input[index]
            full_list.append(i)
            if i not in occurrences:
                occurrences[i] = list()
            occurrences[i].append(index)
        except IndexError:
            i = full_list[index - 1]
            if len(occurrences[i]) == 1:
                if 0 not in occurrences:
                    occurrences[0] = list()
                occurrences[0].append(index)
                full_list.append(0)
            else:
                diff = occurrences[i][-1] - occurrences[i][-2]
                if diff not in occurrences:
                    occurrences[diff] = list()
                occurrences[diff].append(index)
                full_list.append(diff)
        index += 1

    return full_list[-1]


if __name__ == "__main__":
    my_input = [15, 12, 0, 14, 3, 1]
    # my_input = [2,1,3]
    print(part_one(my_input[:]))
