#!/usr/bin/env python3


def clean_input(my_data):
    cleaned_out = []
    for group in my_data:
        cur_entry = str(len(group.split('\n'))) + ":"
        for person in group.split('\n'):
            cur_entry += person
        cleaned_out.append(cur_entry)

    return cleaned_out


def part_one(grouped):
    setted = []
    for group in grouped:
        setted.append(set(group.split(':')[1]))

    summ = 0
    for group_set in setted:
        summ += len(group_set)

    return f'The summ for part one is: {summ}'


def part_two(grouped):
    setted = []
    for group in grouped:
        out_group = ''
        group_count = int(group.split(':')[0])
        for char in group.split(':')[1]:
            char_count = group.count(char)
            if char_count == group_count:
                out_group += char
        setted.append(set(out_group))

    summ = 0
    for group_set in setted:
        summ += len(group_set)

    return f'The summ for part two is: {summ}'


with open('input_6.txt') as f_object:
    my_input = f_object.read().split('\n\n')

cleaned = clean_input(my_input[:])
print(part_one(cleaned[:]))
print(part_two(cleaned[:]))
