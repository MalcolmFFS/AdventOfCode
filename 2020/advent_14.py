#!/usr/bin/env python3


import itertools


def the_setup():
    with open('input_14.txt') as f_object:
        tmp = f_object.read().split('\n')

    instructions = dict()
    for instruction in tmp:
        if 'mask' in instruction:
            cur_mask = instruction.split()[-1]
            instructions[cur_mask] = list()
        elif 'mem' in instruction:
            instructions[cur_mask].append(instruction)

    return instructions


def part_one(the_input):
    def find_36bit_value(dec_num):
        if abs(dec_num) <= 0xFFFFFFFF:
            base_bin_value = format(dec_value, 'b')
            bin_value = ''
            for _ in range(36 - len(base_bin_value)):
                bin_value += '0'
            else:
                bin_value += base_bin_value
        else:
            bin_value = '000000000000000000000000000000000000'

        return bin_value

    def bin_value_after_mask(my_mask, bin_num):
        result_val = ''
        for m, i in zip(my_mask, bin_num):
            if m.lower() == 'x':
                result_val += i
            else:
                result_val += m

        return result_val

    init_program = dict()
    for mask, instructions in the_input.items():
        for instruction in instructions:
            dec_value = int(instruction.split()[-1])
            mem_pos = instruction.split('[')[1].split(']')[0]
            bin_value_36bit = find_36bit_value(dec_value)

            init_program[mem_pos] = bin_value_after_mask(mask, bin_value_36bit)

    complete_values = [int(values, 2) for values in init_program.values()]
    answer = f"The sum of all remaining values in memory is: {sum(complete_values)}."

    return answer


def part_two(the_input):
    def find_36bit_value(dec_num):
        if abs(dec_num) <= 0xFFFFFFFF:
            base_bin_value = format(dec_num, 'b')
            bin_value = ''
            for _ in range(36 - len(base_bin_value)):
                bin_value += '0'
            else:
                bin_value += base_bin_value
        else:
            bin_value = '000000000000000000000000000000000000'

        return bin_value

    def bin_value_after_mask(my_mask, bin_num):
        result_val = ''
        for m, i in zip(my_mask, bin_num):
            if m.lower() == '0':
                result_val += i
            elif m.lower() == '1':
                result_val += '1'
            elif m.lower() == 'x':
                result_val += 'f'

        return result_val

    def split_bin_value(bin_num):
        split_out = list()
        floating_indexes = list()
        for index, char in enumerate(bin_num):
            if char == 'f':
                floating_indexes.append(index)

        possible_combos = itertools.product(['0', '1'], repeat=len(floating_indexes))
        for combo in possible_combos:
            tmp_str = bin_num
            for index, combo_char in zip(floating_indexes, combo):
                tmp_str[index] = combo_char
            split_out.append(''.join(tmp_str))

        return split_out

    init_program = dict()
    for mask, instructions in the_input.items():
        for instruction in instructions:
            dec_value = int(instruction.split()[-1])
            mem_pos = instruction.split('[')[1].split(']')[0]
            bin_value_36bit = find_36bit_value(int(mem_pos))
            post_mask = bin_value_after_mask(mask, bin_value_36bit)
            split_bin_values = split_bin_value(list(post_mask))

            for split_value in split_bin_values:
                init_program[split_value] = dec_value

    complete_values = [int(values) for values in init_program.values()]
    answer = f"The sum of all remaining values in memory is: {sum(complete_values)}."

    return answer


if __name__ == "__main__":
    my_input = the_setup()
    print(part_one(my_input))
    print(part_two(my_input))
