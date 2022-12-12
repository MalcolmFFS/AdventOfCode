#!/usr/bin/env python3

# Output:
# 

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append(line.split())

    return the_input


def manhattan_distance(h, t):
    return sum([abs(h[0] - t[0]), abs(h[1] - t[1])])


def check_tail(head, tail, direction):
    distance = manhattan_distance(head, tail)
    if direction == "U":
        
        if head[0] == tail[0]:
            tail[1] += 1
            return tail
        else:


    return tail

def part_one(the_input: list) -> int:
    head_position = [0, 0]
    tail_positions = [[0,0]]

    for step in the_input:
        direction, n = step

        tail_position = tail_positions[-1]
        if direction == "U":
            # Increase X
            while head_position[0] != head_position[0] + n:
                head_position[0] += 1
                tail_position = check_tail(head_position, tail_position, direction)

        elif direction == "D":
            # Decrease X
            head_position = (head_position[0] - n, head_position[1])
        elif direction == "R":
            # Increase Y
            head_position = (head_position[0], head_position[1] + n)
        elif direction == "L":
            # Decrease Y
            head_position = (head_position[0], head_position[1] - n)

        # for position in tail_steps(direction, head_position, tail_positions[-1]):
        #     tail_positions.append(position)

    return len(set(tail_positions))


def part_two(the_input: list) -> int:
    pass


def main():
    with open('input_09.txt') as f_object:
        input_09 = f_object.read().strip()
    
    # Expected output part 1: 13
    # Expected output part 2: 
    sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_09)
    
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
