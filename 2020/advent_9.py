#!/usr/bin/env python3

from collections import deque
from itertools import combinations

with open('input_9.txt') as f_object:
    my_input = f_object.read().split('\n')

pre = 25
pre_list = deque([],pre)

for line in my_input:
    line = int(line)
    if len(pre_list) < pre:
        pre_list.append(line)
    elif len(pre_list) == pre:
        combo = combinations(pre_list, 2)
        combo_summs = [sum(pair) for pair in combo]
        if line in combo_summs:
            pre_list.append(line)
            continue
        elif line not in combo_summs:
            print(f'This number broke the pattern! ({line})')
            goal = line
            break


i = 2
while i < 1001:
    tmp_list = deque([],i)
    for line in my_input:
        line = int(line)
        if len(tmp_list) < i:
            tmp_list.append(line)
            continue
        elif len(tmp_list) == i:
            if sum(tmp_list) == goal:
                out_list = [j for j in tmp_list]
                print(f'{len(out_list)}: {out_list}')
                print(f'Min: {min(out_list)}; Max: {max(out_list)}')
                print(f'Summ: {min(out_list) + max(out_list)}')
                raise SystemExit()
            else:
                tmp_list.append(line)
                continue
    i += 1
    continue