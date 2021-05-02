#!/usr/bin/env python3


def binaryToDecimal(n):
    return int(n,2)


my_input = []
with open('input_5.txt') as f_object:
    for line in f_object:
        my_input.append(str(line.strip()))

seats = []
for seat in my_input:
    row_str = ''
    column_str = ''
    for char in seat:
        if char == 'F':
            row_str += '0'
        elif char == 'B':
            row_str += '1'
        elif char == 'L':
            column_str += '0'
        elif char == 'R':
            column_str += '1'
    row = binaryToDecimal(row_str)
    column = binaryToDecimal(column_str)

    seats.append([row,column,row * 8 + column])

ids = []
for x,y,z in seats:
    ids.append(z)

print(f'Highest flight ID: {max(ids)}')
for i in range(914):
    if i not in ids and i - 1 in ids and i + 1 in ids:
        print(f'ID {i} is missing!')
