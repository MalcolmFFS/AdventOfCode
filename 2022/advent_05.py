#!/usr/bin/env python3

# Output:
# The top of each stack if using the CrateMover 9000 (part one) is: TGWSMRBPN.
# The top of each stack if using the CrateMover 9001 (part two) is: TZLTLWRNF.

def the_setup(data: str) -> list:
    the_input = list()
    stacks = list()

    for i in data.split('\n\n')[0].split('\n'):
        stacks.append([i[x:x + 4] for x in range(0, len(i), 4)])

    stacks.reverse()
    stacks_dict = dict()
    for row in stacks:
        for col_idx, col in enumerate(row, 1):
            if col_idx not in stacks_dict and '[' in col:
                stacks_dict[int(col_idx)] = [col.strip('[] ')]
            elif col_idx in stacks_dict and '[' in col:
                stacks_dict[int(col_idx)].append(col.strip('[] '))

    the_input.append(stacks_dict)

    for line in data.split('\n\n')[1].split('\n'):
        _, quantity, _, from_col, _, to_col = line.split(' ')
        the_input.append((int(quantity), int(from_col), int(to_col)))

    return the_input


def part_one(the_input: list) -> str:
    stacks = {key: value[:] for key, value in the_input[0].items()}
    steps = the_input[1:]

    for step in steps:
        quantity, from_col, to_col = step
        for _ in range(quantity):
            crate = stacks[from_col].pop()
            stacks[to_col].append(crate)

    output = str()
    for stack in stacks.keys():
        output += stacks[stack][-1]

    return output


def part_two(the_input: list) -> str:
    stacks = {key: value[:] for key, value in the_input[0].items()}
    steps = the_input[1:]

    for step in steps:
        quantity, from_col, to_col = step
        crates = stacks[from_col][-quantity:]
        for crate in crates:
            stacks[from_col].pop()
            stacks[to_col].append(crate)

    output = str()
    for stack in stacks.keys():
        output += stacks[stack][-1]

    return output


def main():
    with open('input_05.txt') as f_object:
        input_05 = f_object.read().strip('\n')

    # Since formatting gets lost when in a string. Visual comment.
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3
    #
    # move 1 from 2 to 1
    # move 3 from 1 to 3
    # move 2 from 2 to 1
    # move 1 from 1 to 2
    sample_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_05)

    print(f"The top of each stack if using the CrateMover 9000 (part one) is: {part_one(my_input)}.")
    print(f"The top of each stack if using the CrateMover 9001 (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
