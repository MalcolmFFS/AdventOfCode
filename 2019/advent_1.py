#!/usr/bin/env python3


def calculate_fuel(task, modules):
    total_fuel = 0
    for module in modules:
        fuel = (module // 3) - 2
        if task == 'pt2':
            while fuel > 0:
                total_fuel += fuel
                fuel = (fuel // 3) - 2
        elif task == 'pt1':
            total_fuel += fuel
    return total_fuel


my_input = []

with open('input_1.txt') as f_object:
    for line in f_object:
        my_input.append(int(line))

print(f"Part One: {calculate_fuel('pt1',my_input[:])}")
print(f"Part Two: {calculate_fuel('pt2',my_input[:])}")
