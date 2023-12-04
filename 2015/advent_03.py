#!/usr/bin/env python3

# Output:
# The number of houses that got at least one present from just Santa (part one) is: 2592.
# The number of houses that got at least one present from Santa and Robo-Santa (part two) is: 2360.

def the_setup(data: str) -> list:
    the_input = list(data)

    return the_input


def part_one(the_input: list) -> int:
    unique_houses = {(0, 0)}
    cur_pos = [0, 0]

    for char in the_input:
        if char == "^":
            cur_pos = [cur_pos[0], cur_pos[1] + 1]
        elif char == ">":
            cur_pos = [cur_pos[0] + 1, cur_pos[1]]
        elif char == "v":
            cur_pos = [cur_pos[0], cur_pos[1] - 1]
        elif char == "<":
            cur_pos = [cur_pos[0] - 1, cur_pos[1]]

        if tuple(cur_pos) not in unique_houses:
            unique_houses.add(tuple(cur_pos))


    return len(unique_houses)


def part_two(the_input: list) -> int:
    who = ["santa", "robo-santa"]

    unique_houses = {
        "santa": {(0, 0)},
        "robo-santa": {(0, 0)}
    }
    positions = {
        "santa": [0, 0],
        "robo-santa": [0, 0]
    }

    count = 0
    for char in the_input:
        whos_moving = who[count % 2]
        if char == "^":
            positions[whos_moving] = [positions[whos_moving][0], positions[whos_moving][1] + 1]
        elif char == ">":
            positions[whos_moving] = [positions[whos_moving][0] + 1, positions[whos_moving][1]]
        elif char == "v":
            positions[whos_moving] = [positions[whos_moving][0], positions[whos_moving][1] - 1]
        elif char == "<":
            positions[whos_moving] = [positions[whos_moving][0] - 1, positions[whos_moving][1]]

        if tuple(positions[whos_moving]) not in unique_houses[whos_moving]:
            unique_houses[whos_moving].add(tuple(positions[whos_moving]))

        count += 1

    for house in unique_houses["robo-santa"]:
        if house not in unique_houses["santa"]:
            unique_houses["santa"].add(house)

    return len(unique_houses["santa"])


def main():
    with open('input_03.txt') as f_object:
        input_03 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """^v"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_03)
    
    print(f"The number of houses that got at least one present from just Santa (part one) is: {part_one(my_input)}.")
    print(f"The number of houses that got at least one present from Santa and Robo-Santa (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
