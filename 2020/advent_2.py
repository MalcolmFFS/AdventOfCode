#!/usr/bin/env python3

## Output
# Part One:
# 	Total Passwords: 1000
# 	Valid Passwords: 506
# 	Invalid Passwords: 494
# 	FAILED Passwords: 0
#
# Part Two:
# 	Total Passwords: 1000
# 	Valid Passwords: 443
# 	Invalid Passwords: 557
# 	FAILED Passwords: 0

def part_one(total):
    valid = []
    valid_ct = 0
    invalid = []
    invalid_ct = 0
    failed = []
    failed_ct = 0
    total_ct = len(total)

    for item in total:
        x, y, z = item.split()
        y = y[0]
        x_min, x_max = x.split('-')
        x_min, x_max = int(x_min), int(x_max)
        if z.count(y) >= x_min and z.count(y) <= x_max:
            valid.append(item)
            valid_ct += 1
        elif z.count(y) < x_min or z.count(y) > x_max:
            invalid.append(item)
            invalid_ct += 1
        else:
            failed.append(item)
            failed_ct += 1

    to_return = f'Part One:\n'
    to_return += f'\tTotal Passwords: {str(total_ct)}\n'
    to_return += f'\tValid Passwords: {str(valid_ct)}\n'
    to_return += f'\tInvalid Passwords: {str(invalid_ct)}\n'
    to_return += f'\tFAILED Passwords: {str(failed_ct)}\n'

    return to_return


def part_two(total):
    valid = []
    valid_ct = 0
    invalid = []
    invalid_ct = 0
    failed = []
    failed_ct = 0
    total_ct = len(total)

    for item in total:
        x, y, z = item.split()
        y = y[0]
        x1, x2 = x.split('-')
        x1, x2 = int(x1) - 1, int(x2) - 1

        match_count = 0

        if z[x1] == y: match_count += 1
        if z[x2] == y: match_count += 1
        if match_count == 1:
            valid.append(item)
            valid_ct += 1
        elif match_count == 0 or match_count == 2:
            invalid.append(item)
            invalid_ct += 1
        else:
            failed.append(item)
            failed_ct += 1

    to_return = f'Part Two:\n'
    to_return += f'\tTotal Passwords: {str(total_ct)}\n'
    to_return += f'\tValid Passwords: {str(valid_ct)}\n'
    to_return += f'\tInvalid Passwords: {str(invalid_ct)}\n'
    to_return += f'\tFAILED Passwords: {str(failed_ct)}\n'

    return to_return


total = []

with open('input_2.txt') as f_object:
    for line in f_object:
        total.append(str(line.strip()))

print(part_one(total))
print(part_two(total))


