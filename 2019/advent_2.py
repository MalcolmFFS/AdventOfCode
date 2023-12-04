#!/usr/bin/env python3


from itertools import islice, permutations


def setup_intcode(input_code):
    intcode_dict = {}
    for idx, code in islice(enumerate(input_code), None):
        intcode_dict[idx] = int(code)

    return intcode_dict


def run_intcode(intcode, noun, verb):
    opcodes = [0]

    memory = intcode.copy()
    memory[1], memory[2] = noun, verb

    for instruction in opcodes:
        try:
            pos1 = memory[instruction + 1]
            pos2 = memory[instruction + 2]
            pos3 = memory[instruction + 3]
        except KeyError:
            pass
        if memory[instruction] == 1:
            computed_value = memory[pos1] + memory[pos2]
            opcodes.append(instruction + 4)
        elif memory[instruction] == 2:
            computed_value = memory[pos1] * memory[pos2]
            opcodes.append(instruction + 4)
        elif memory[instruction] == 99:
            opcodes.append(instruction + 1)
            break
        else:
            raise Exception(f"IntCode error with the opcode {memory[instruction]} at pos {instruction}")

        memory[pos3] = computed_value

    return memory


if __name__ == "__main__":
    my_input = []

    with open('input_2.txt') as f_object:
        for line in f_object:
            my_input = line.split(',')

    intcode = setup_intcode(my_input)

    noun, verb = 12, 2
    part1 = run_intcode(intcode, noun, verb)
    print(f'With noun {noun} and verb {verb}, the output is {part1[0]}')

    part2_list = range(0, 100)
    goal = 19690720
    for permutation in permutations(part2_list, 2):
        noun, verb = permutation
        part2 = run_intcode(intcode, noun, verb)
        if part2[0] == goal:
            print(f"Output of {goal} is achieved with noun {noun} and verb {verb}.")
            print(f"100 * {noun} + {verb} = {100 * noun + verb}")
        else:
            continue
