#!/usr/bin/env python3


def do_the_iterate_again(my_list):
    for l in range(len(my_list) - 1):
        r = len(my_list) - 1
        while l < r:
            s = my_list[l] + my_list[r]
            if s < 2020:
                l += 1
            elif s > 2020:
                r -= 1
            else:
                return my_list[l], my_list[r], my_list[l] * my_list[r]

    return "failed"


def do_the_iterate_again_ptTwo(my_list):
    for i in range(len(my_list) - 2):
        l, r = i+1, len(my_list)-1
        while l < r:
            s = my_list[i] + my_list[l] + my_list[r]
            if s < 2020:
                l += 1
            elif s > 2020:
                r -= 1
            elif s == 2020:
                return my_list[l], my_list[i], my_list[r], (my_list[i] * my_list[r] * my_list[l])


my_list = []

with open('input_1.txt') as f_object:
    for line in f_object:
        my_list.append(int(line.strip()))

my_list.sort()
print(do_the_iterate_again(my_list))
print(do_the_iterate_again_ptTwo(my_list))
