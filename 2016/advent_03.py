#!/usr/bin/env python3

from collections import deque

# Output:
# 

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append([int(i) for i in line.split()])

    return the_input


def part_one(the_input: list) -> int:
    possible = 0
    for triangle in the_input:
        a, b, c = triangle
        if a + b > c and c + b > a and a + c > b:
            possible += 1
            continue

    return possible

def part_two(the_input: list) -> int:
    triangles = deque(maxlen=3)
    new_triangles = []

    for line in the_input:
        if len(triangles) < 3:
            triangles.append(line)

        if len(triangles) == 3:
            new_triangles.append([triangles[0][0], triangles[1][0], triangles[2][0]])
            new_triangles.append([triangles[0][1], triangles[1][1], triangles[2][1]])
            new_triangles.append([triangles[0][2], triangles[1][2], triangles[2][2]])
            triangles.pop()
            triangles.pop()
            triangles.pop()

    return part_one(new_triangles)


def main():
    with open('input_03.txt') as f_object:
        input_03 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_03)
    
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
