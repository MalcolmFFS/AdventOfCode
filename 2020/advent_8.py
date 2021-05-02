#!/usr/bin/env python3


def execute_input(my_input):
    accumulator = 0
    i = 0
    while True:
        try:
            cmd = my_input[i].split()[0]
            cmd_arg = int(my_input[i].split()[1])
            if cmd == 'acc':
                accumulator += cmd_arg
                i += 1
                yield accumulator,{i:my_input[i]}
                continue
            elif cmd == 'jmp':
                i += cmd_arg
                yield accumulator,{i:my_input[i]}
                continue
            elif cmd == 'nop':
                i += 1
                yield accumulator,{i:my_input[i]}
                continue
        except IndexError:
            print(f'Part Two: Execution complete. Accumulator: {accumulator}')
            raise SystemExit()


def part_one(v,my_input):
    output = []
    for accumulator, line in execute_input(my_input):
        if line in output:
            if v:
                print(f'Part One: Execution broke on line {line}')
                print(f'Part One: Current accumulator value: {accumulator}')
            return False
        elif line not in output:
            output.append(line)

    print(f'Current accumulator value: {accumulator}')
    return True


def part_two(my_input):
        nops = []
        jmps = []
        for i,line in enumerate(my_input):
            if 'nop' in line:
                nops.append(i)
            elif 'jmp' in line:
                jmps.append(i)

        for i in nops:
            nop_arg = my_input[i].split()[1]
            my_input[i] = f'jmp {nop_arg}'
            if part_one(False,my_input[:]):
                raise SystemExit()
            elif not part_one(False,my_input[:]):
                my_input[i] = f'nop {nop_arg}'

        for i in jmps:
            jmp_arg = my_input[i].split()[1]
            my_input[i] = f'nop {jmp_arg}'
            if part_one(False,my_input[:]):
                continue
            elif not part_one(False,my_input[:]):
                my_input[i] = f'jmp {jmp_arg}'


if __name__ == "__main__":
    with open('input_8.txt') as f_object:
        my_input = f_object.read().split('\n')

    part_one(True,my_input[:])
    part_two(my_input[:])
