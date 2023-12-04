#!/usr/bin/env python3


def steps_between_cross(cross_points, path1, path2):
    steps = {}
    for point in cross_points:

        index = 0
        for step in path1:
            index += 1
            if step == point:
                steps[point] = index
                break

        index = 0
        for step in path2:
            index += 1
            if step == point:
                steps[point] += index
                break

    return min([i for i in steps.values()])


def shortest_manhattan_distance(goal, points):
    distances = []

    x1, y1 = goal
    for point in points:
        x2, y2 = point
        distance = abs(x1 - x2) + abs(y1 - y2)
        distances.append((distance, point))

    return min([i[0] for i in distances])


def trace_path_coordinates(steps):
    path = []
    x, y = 0, 0

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        if direction == 'R':
            for _ in range(distance):
                x += 1
                path.append((x, y))
        elif direction == 'L':
            for _ in range(distance):
                x -= 1
                path.append((x, y))
        elif direction == 'U':
            for _ in range(distance):
                y += 1
                path.append((x, y))
        elif direction == 'D':
            for _ in range(distance):
                y -= 1
                path.append((x, y))
        else:
            break

    return path


if __name__ == "__main__":
    my_input = []

    with open('input_3.txt') as f_object:
        for line in f_object:
            my_input.append(line)

    wire_1 = my_input[0].split(',')
    wire_2 = my_input[1].split(',')

    wire_path_1 = trace_path_coordinates(wire_1)
    wire_path_2 = trace_path_coordinates(wire_2)

    cross_points = set(wire_path_1) & set(wire_path_2)

    print(f'The shortest distance is: {shortest_manhattan_distance((0, 0), cross_points)}.')

    shortest_path_to_cross = steps_between_cross(cross_points, wire_path_1, wire_path_2)
    print(f'The shortest amount of steps to first cross is {shortest_path_to_cross}.')
