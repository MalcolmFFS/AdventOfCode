#!/usr/bin/env python3


def the_setup():
    with open('input_12.txt') as f_object:
        the_input = f_object.read().split('\n')

    return the_input


def part_one(the_input):
    # 0 = north, 1 = east, 2 = south, 3 = west
    directions = {0: 0, 1: 0, 2: 0, 3: 0}
    facing = 1
    for instruction in the_input:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == 'F':
            directions[facing] += distance
        elif direction == 'R':
            if distance == 90:
                facing = (facing + 1) % 4
            elif distance == 180:
                facing = (facing + 2) % 4
            elif distance == 270:
                facing = (facing + 3) % 4
        elif direction == 'L':
            if distance == 90:
                facing = (facing - 1) % 4
            elif distance == 180:
                facing = (facing - 2) % 4
            elif distance == 270:
                facing = (facing - 3) % 4
        elif direction == 'N':
            directions[0] += distance
        elif direction == 'E':
            directions[1] += distance
        elif direction == 'S':
            directions[2] += distance
        elif direction == 'W':
            directions[3] += distance

    return abs(directions[0] - directions[2]) + abs(directions[1] - directions[3])


def part_two(the_input):
    # 0 = north, 1 = east, 2 = south, 3 = west
    ship = {0: 0, 1: 0, 2: 0, 3: 0}
    waypoint = {0: 1, 1: 10, 2: 0, 3: 0}
    for instruction in the_input:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == 'F':
            for key, value in waypoint.items():
                ship[key] += value * distance
        elif direction == 'R':
            tmp_waypoint = waypoint.copy()
            if distance == 90:
                for key, value in tmp_waypoint.items():
                    waypoint[(key + 1) % 4] = value
            elif distance == 180:
                for key, value in tmp_waypoint.items():
                    waypoint[(key + 2) % 4] = value
            elif distance == 270:
                for key, value in tmp_waypoint.items():
                    waypoint[(key + 3) % 4] = value
        elif direction == 'L':
            tmp_waypoint = waypoint.copy()
            if distance == 90:
                for key, value in tmp_waypoint.items():
                    waypoint[(key - 1) % 4] = value
            elif distance == 180:
                for key, value in tmp_waypoint.items():
                    waypoint[(key - 2) % 4] = value
            elif distance == 270:
                for key, value in tmp_waypoint.items():
                    waypoint[(key - 3) % 4] = value
        elif direction == 'N':
            waypoint[0] += distance
        elif direction == 'E':
            waypoint[1] += distance
        elif direction == 'S':
            waypoint[2] += distance
        elif direction == 'W':
            waypoint[3] += distance

    return abs(ship[0] - ship[2]) + abs(ship[1] - ship[3])


if __name__ == "__main__":
    my_input = the_setup()
    # my_input = [
    #     'F10',
    #     'N3',
    #     'F7',
    #     'R90',
    #     'F11'
    # ]
    manhattan = part_one(my_input)
    print(f"Manhattan distance for part one: {manhattan}.")

    manhattan = part_two(my_input)
    print(f"Manhattan distance for part two: {manhattan}.")
