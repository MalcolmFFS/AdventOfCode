#!/usr/bin/env python3


import sys
from itertools import islice, permutations


def setup_intcode(input_code):
    intcode_dict = {}
    for idx, code in islice(enumerate(input_code), None):
        intcode_dict[idx] = int(code)

    return intcode_dict


def run_intcode(intcode):
    instructions = [0]
    computed_value = None
    systems = {
        1: "air conditioning unit",
        5: "thermal radiator controller"
    }

    memory = intcode.copy()

    for instruction in instructions:
        # print(f"Instruction index: {instructions[-1]}")
        full_instruction = str(memory[instruction])
        opcode = int(full_instruction[-2:])
        # print(f"Instruction opcode: {opcode}")

        if len(full_instruction) > 2:
            try:
                mode_3, mode_2, mode_1 = [int(i) for i in full_instruction[:-2]]
            except ValueError:
                try:
                    mode_2, mode_1 = [int(i) for i in full_instruction[:-2]]
                    mode_3 = 0
                except ValueError:
                    mode_1 = int(full_instruction[:-2])
                    mode_2, mode_3 = 0, 0
        else:
            mode_1, mode_2, mode_3 = 0, 0, 0

        # print(f"Modes: {mode_1, mode_2, mode_2}")

        if opcode == 1:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction +2
            if mode_3 == 0:
                pos3 = memory[instruction + 3]
            elif mode_3 == 1:
                pos3 = instruction +3

            computed_value = memory[pos1] + memory[pos2]
            memory[pos3] = computed_value
            instructions.append(instruction + 4)

        elif opcode == 2:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction + 2
            if mode_3 == 0:
                pos3 = memory[instruction + 3]
            elif mode_3 == 1:
                pos3 = instruction + 3

            computed_value = memory[pos1] * memory[pos2]
            memory[pos3] = computed_value
            instructions.append(instruction + 4)

        elif opcode == 3:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1

            # print(f"Opcode {opcode} positions. Pos1: {pos1};")

            while not isinstance(computed_value, int):
                try:
                    print("Systems:")
                    for key, value in systems.items():
                        print(f"\t{key}: {value.title()}.")
                    computed_value = int(input('Please select a system to diagnose -> '))
                    if computed_value in systems:
                        print(f"'{systems[computed_value].title()}' selected!")
                    else:
                        computed_value = None
                        continue
                    memory[pos1] = computed_value
                    instructions.append(instruction + 2)
                except ValueError:
                    print("You entered a non-integer value, try again...")
                    continue

        elif opcode == 4:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1

            print(f"Opcode 4 output: {memory[pos1]}.")
            instructions.append(instruction + 2)

        elif opcode == 5:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction + 2

            # print(f"Opcode {opcode} positions. Pos1: {pos1}; Pos2: {pos2}")

            if memory[pos1] != 0:
                instructions.append(memory[pos2])
            else:
                instructions.append(instruction + 3)

        elif opcode == 6:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction + 2

            # print(f"Opcode {opcode} positions. Pos1: {pos1}; Pos2: {pos2}")

            if memory[pos1] == 0:
                instructions.append(memory[pos2])
            else:
                instructions.append(instruction + 3)

        elif opcode == 7:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction +2
            if mode_3 == 0:
                pos3 = memory[instruction + 3]
            elif mode_3 == 1:
                pos3 = instruction +3

            if memory[pos1] < memory[pos2]:
                memory[pos3] = 1
            else:
                memory[pos3] = 0

            instructions.append(instruction + 4)

        elif opcode == 8:
            if mode_1 == 0:
                pos1 = memory[instruction + 1]
            elif mode_1 == 1:
                pos1 = instruction + 1
            if mode_2 == 0:
                pos2 = memory[instruction + 2]
            elif mode_2 == 1:
                pos2 = instruction +2
            if mode_3 == 0:
                pos3 = memory[instruction + 3]
            elif mode_3 == 1:
                pos3 = instruction +3

            if memory[pos1] == memory[pos2]:
                memory[pos3] = 1
            else:
                memory[pos3] = 0

            instructions.append(instruction + 4)

        elif opcode == 99:
            instructions.append(instruction + 2)
            break

        else:
            raise Exception(f"IntCode error with the opcode {opcode} at pos {instruction}")

    return memory


if __name__ == "__main__":
    my_input = []

    with open('input_5.txt') as f_object:
        for line in f_object:
            for i in line.strip().split(','):
                my_input.append(i)

    intcode = setup_intcode(my_input)
    run_intcode(intcode)
