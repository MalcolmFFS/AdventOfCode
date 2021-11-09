#!/usr/bin/env python3


from functools import cache


@cache
def trace_path(pair, pairs, count):
    count += 1
    print(pair, pairs[0:2], count)
    orbitted, orbitter = pair
    count += trace_path(orbitted, pairs, count)

    return count


pairs = []
orbits = {}
orbits['SNP'] = 1

with open('input_6.txt') as f_object:
    for line in f_object:
        orbitted, orbitter = line.strip().split(')')
        pairs.append((orbitted, orbitter))

count = 0
pairs = tuple(pairs)
# print(pairs)
for pair in pairs:
    # print(pair)
    print(pair, pairs[0], count)
    count += trace_path(pair, pairs, count)

print(count)