#!/usr/bin/env python3


def the_setup():
    with open('input_13.txt') as f_object:
        tmp = f_object.read().split('\n')

    start_time, the_input = int(tmp[0]), tmp[1].split(',')
    return start_time, the_input


def part_one(start_time, the_input):
    buses = [int(i) for i in the_input if i != 'x']
    buses_dict = dict()

    for bus in buses:
        # start_time % bus returns remainder since last departure
        # subtracting bus and abs() makes it time til next departure, instead of previous.
        buses_dict[bus] = abs(start_time % bus - bus)

    shortest_wait = min(buses_dict, key=buses_dict.get)

    answer = f"The shortest wait ({shortest_wait}) * the bus id ({buses_dict[shortest_wait]}): "
    answer += f"{shortest_wait * buses_dict[shortest_wait]}"
    return answer


def part_two(the_input):
    remainders = dict()
    # index = net minute from t bus has to arrive; bus = modulo of bus
    for index, bus in enumerate(the_input):
        try:
            remainders[index] = int(bus)
        except ValueError:
            continue

    # This is annoying
    return remainders


if __name__ == "__main__":
    starting_time, my_input = the_setup()
    print(part_one(starting_time, my_input[:]))
    print(part_two(my_input[:]))
