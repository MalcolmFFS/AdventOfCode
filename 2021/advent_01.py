#!/usr/bin/env python3

# The total of times the measurement increased was: 1374.
# The total of times the measurement sum increased was: 1418.


# import timeit


def the_setup():
    the_input = list()
    with open('input_01.txt') as f_object:
        for line in f_object:
            the_input.append(int(line.strip()))

    return the_input


def part_one(the_input):
    increased_count = 0
    for index, i in enumerate(the_input):
        if index != 0:
            if i > the_input[index - 1]:
                increased_count += 1

    return increased_count


def part_two(the_input):
    increased_count = 0
    measurement_sums = list()
    for index, i in enumerate(the_input):
        try:
            next_one = the_input[index + 1]
            next_two = the_input[index + 2]
            measurement_sums.append(i + next_one + next_two)
        except IndexError:
            break

    previous = None
    for measurement_sum in measurement_sums:
        if previous is None:
            previous = measurement_sum
        else:
            if measurement_sum > previous:
                increased_count += 1

            previous = measurement_sum

    return increased_count


# def part_two_nolan(the_input):
#     last3 = []
#     a = b = i = count = 0
#     for num in the_input:
#         last3.append(num)
#         if 2 < i:
#             last3 = last3[1:]
#             a = b
#             b = sum(last3)
#             if a < b:
#                 count += 1
#         else:
#             b = sum(last3)
#         i += 1
#
#     return count


# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#     return wrapped


sample_input = r"""
199
200
208
210
200
207
240
269
260
263"""


if __name__ == "__main__":
    my_input = the_setup()

    # To run against sample input
    # my_input = [int(i) for i in sample_input.strip().split('\n')]

    print(f"The total of times the measurement increased was: {part_one(my_input)}.")
    print(f"The total of times the measurement sum increased was: {part_two(my_input)}.")

    # wrapped_a = wrapper(part_two, my_input)
    # print(timeit.timeit(wrapped_a, number=10000))
    #
    # wrapped_b = wrapper(part_two_nolan, my_input)
    # print(timeit.timeit(wrapped_b, number=10000))

    # Output of timing mine vs nolan's part two
    # 4.523794
    # 5.5383819
