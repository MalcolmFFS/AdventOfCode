#!/usr/bin/env python3


import time


def the_setup():
    with open('input_10.txt') as f_object:
        the_input = f_object.read().split('\n')

    for index, _ in enumerate(the_input):
        the_input[index] = int(the_input[index])
    else:
        the_input.sort()

    your_device = the_input[-1] + 3
    the_input.insert(len(the_input), your_device)
    the_input.insert(0, 0)

    return the_input


def part_one(the_input):
    out_dict = {1: [], 2: [], 3: []}

    for adapter in the_input:
        if adapter == 0:
            cur_jolt = 0
            continue
        jolt_diff = adapter - cur_jolt
        if jolt_diff in out_dict:
            out_dict[jolt_diff].append(adapter)
            cur_jolt = adapter
        else:
            print(cur_jolt, adapter)

    return out_dict


def part_two(the_input):
    def do_the_recurse(index):
        my_count = 0
        options = tmp_dict[index]
        if len(options) > 0:
            for x in options:
                if x in possibilities_dict:
                    my_count += possibilities_dict[x]
                else:
                    my_count += do_the_recurse(x)
                    possibilities_dict[x] = my_count
        else:
            my_count += 1

        return my_count

    tmp_dict = dict()
    for i in the_input:
        tmp_dict[i] = []
        for j in range(1, 4):
            if i + j in the_input:
                tmp_dict[i].append(i + j)

    possibilities_dict = dict()
    possibilities_count = do_the_recurse(the_input[0])

    return possibilities_count


if __name__ == "__main__":
    my_input = the_setup()
    part_one_dict = part_one(my_input[:])

    print(f"Adapters with difference of 1: {len(part_one_dict[1])}.")
    print(f"Adapters with difference of 3: {len(part_one_dict[3])}.")
    print(f"Diff 1 and diff 3 multiplied = {len(part_one_dict[1]) * len(part_one_dict[3])}.")

    tic = time.perf_counter()
    part_two_out = part_two(my_input[:])
    toc = time.perf_counter()
    print(f"Time required with memoization: {toc - tic}")
    print(f"Total possible combinations of adapters: {part_two_out}.")
