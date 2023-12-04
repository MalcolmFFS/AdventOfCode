#!/usr/bin/env python3

# Output:
# The Easter Bunny HQ's manhattan distance with first method (part one) is: 246.
# The Easter Bunny HQ's manhattan distance with second method (part two) is: 124.

def the_setup(data: str) -> list:
    the_input = list()
    for instruction in data.split(','):
        the_input.append(instruction.strip())

    return the_input


def manhattan_distance(a, b):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1])])


def part_one(the_input: list) -> int:
    position = [0, 0]
    directions = ["north", "east", "south", "west"]
    cur_direction = 0

    for instruction in the_input:
        if instruction.startswith("R"):
            cur_direction += 1
        elif instruction.startswith("L"):
            cur_direction -= 1

        if directions[cur_direction % 4] == "north":
            position[1] += int(instruction[1:])
        elif directions[cur_direction % 4] == "south":
            position[1] -= int(instruction[1:])
        elif directions[cur_direction % 4] == "east":
            position[0] += int(instruction[1:])
        elif directions[cur_direction % 4] == "west":
            position[0] -= int(instruction[1:])

    return manhattan_distance([0, 0], position)


def part_two(the_input: list) -> int:
    position = [0, 0]
    directions = ["north", "east", "south", "west"]
    cur_direction = 0
    past_positions = list()

    for instruction in the_input:
        if instruction.startswith("R"):
            cur_direction += 1
        elif instruction.startswith("L"):
            cur_direction -= 1

        orig_position = position[:]

        if directions[cur_direction % 4] == "north":
            while position[1] < orig_position[1] + int(instruction[1:]):
                position[1] += 1
                if position in past_positions:
                    return manhattan_distance([0, 0], position)
                else:
                    past_positions.append(position[:])

        elif directions[cur_direction % 4] == "south":
            while position[1] > orig_position[1] - int(instruction[1:]):
                position[1] -= 1
                if position in past_positions:
                    return manhattan_distance([0, 0], position)
                else:
                    past_positions.append(position[:])

        elif directions[cur_direction % 4] == "east":
            while position[0] < orig_position[0] + int(instruction[1:]):
                position[0] += 1
                if position in past_positions:
                    return manhattan_distance([0, 0], position)
                else:
                    past_positions.append(position[:])

        elif directions[cur_direction % 4] == "west":
            while position[0] > orig_position[0] - int(instruction[1:]):
                position[0] -= 1
                if position in past_positions:
                    return manhattan_distance([0, 0], position)
                else:
                    past_positions.append(position[:])


def main():
    with open('input_01.txt') as f_object:
        input_01 = f_object.read().strip()

    # Expected output part 1: 8
    # Expected output part 2: 4
    sample_input = """R8, R4, R4, R8"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_01)

    print(f"The Easter Bunny HQ's manhattan distance with first method (part one) is: {part_one(my_input)}.")
    print(f"The Easter Bunny HQ's manhattan distance with second method (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
