#!/usr/bin/env python3

# Output:
# The sum of the risk levels of all low points (part one) is: 496.
# The product of the three largest basins (part two) is: 902880.

# advent_09.py
# part_one():
# real    0m0.030s
# part_two()
# real    0m2.701s


def the_setup() -> list:
    the_input = list()
    with open('input_09.txt') as f_object:
        tmp = f_object.read().split('\n')
        for line in tmp:
            the_input.append([int(i) for i in line])

    return the_input


def part_one(the_input: list, main_call: bool = True):
    low_points = []
    for r_index, row in enumerate(the_input):
        for c_index, col in enumerate(row):
            if r_index != 0:
                if the_input[r_index - 1][c_index] <= col:
                    continue
            if c_index != len(row) - 1:
                if the_input[r_index][c_index + 1] <= col:
                    continue
            if r_index != len(the_input) - 1:
                if the_input[r_index + 1][c_index] <= col:
                    continue
            if c_index != 0:
                if the_input[r_index][c_index - 1] <= col:
                    continue
            low_points.append((col, (r_index, c_index)))

    if main_call:
        return sum(x[0] for x in low_points) + len(low_points)
    else:
        return low_points


def part_two(the_input: list) -> int:
    def calculate_basin(point: tuple) -> list:
        r, c = point
        r_max = len(the_input) - 1
        c_max = len(the_input[0]) - 1
        done.append(point)
        steps = []
        if r != 0:
            step = (r - 1, c)
            if step not in done and the_input[step[0]][step[1]] != 9:
                steps.append(step)
                steps.extend(calculate_basin(step))
            elif step not in done and the_input[step[0]][step[1]] == 9:
                done.append(step)
        if c != 0:
            step = (r, c - 1)
            if step not in done and the_input[step[0]][step[1]] != 9:
                steps.append(step)
                steps.extend(calculate_basin(step))
            elif step not in done and the_input[step[0]][step[1]] == 9:
                done.append(step)
        if r != r_max:
            step = (r + 1, c)
            if step not in done and the_input[step[0]][step[1]] != 9:
                steps.append(step)
                steps.extend(calculate_basin(step))
            elif step not in done and the_input[step[0]][step[1]] == 9:
                done.append(step)
        if c != c_max:
            step = (r, c + 1)
            if step not in done and the_input[step[0]][step[1]] != 9:
                steps.append(step)
                steps.extend(calculate_basin(step))
            elif step not in done and the_input[step[0]][step[1]] == 9:
                done.append(step)

        return steps

    low_points = part_one(the_input, main_call=False)
    done = list()
    basins = {k[1]: [k[1]] for k in low_points}
    for low_point in low_points:
        basins[low_point[1]].extend(calculate_basin(low_point[1]))

    lengths = [len(v) for v in basins.values()]

    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def main():
    sample_input = r"""
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    """

    # To run against sample input
    # samp_input = list()
    # for line in sample_input.strip().split('\n'):
    #     samp_input.append([int(i) for i in line.strip()])
    #
    # print(f"The  (part one) is: {part_one(samp_input)}.")
    # print(f"The  (part two) is: {part_two(samp_input)}.")

    my_input = the_setup()
    print(f"The sum of the risk levels of all low points (part one) is: {part_one(my_input)}.")
    print(f"The product of the three largest basins (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
