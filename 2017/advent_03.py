#!/usr/bin/env python3

# Output:
# 

def the_setup(data: str) -> int:
    return int(data)


def manhattan_distance(a, b):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1])])


def part_one(the_input: int) -> int:
    # Honestly this would take too long to walk, and I'm noob, so I googled to educate
    # I'm using the "perfect squares as anchors" method that was used
    # here: https://github.com/jwoLondon/adventOfCode/blob/master/2017/d03_2017.md
    # I've not read the actual code, just the premise of the solution.

    # First get a list of all perfect squares of odds, not using division.
    # Until one passes target.
    perfect_squres_of_odds = set()
    for n in range(1, int(the_input ** 0.5)):
        square = n ** 2
        if n % 2 == 0:
            continue
        if square > the_input:
            perfect_squres_of_odds.add(square)
            break

        perfect_squres_of_odds.add(square)

    # 1 isn't an anchor, it's 0,0, not needed, simpler without it.
    perfect_squres_of_odds.remove(1)

    # Every bottom right corner "anchor" adds 2 manhattan distance from 1
    base_distance = len(perfect_squres_of_odds) * 2
    # Next we'll need to figure where our input stands in relation to our highest square

    # If our grid starts at (0, 0), this is the max on + and - side it'll go
    half_grid = len(perfect_squres_of_odds)


    print(sorted(perfect_squres_of_odds))
    print(len(perfect_squres_of_odds))
    print(the_input - max(perfect_squres_of_odds))

    # Starting on bottom right, and increasing the position
    current = max(perfect_squres_of_odds)
    # Up to 0 decreases distance to 0, 0
    for _ in range(half_grid):
        base_distance -= 1
        current += 1
        if current == the_input:
            return base_distance

    # Up beyond 0 increases distance
    for _ in range(half_grid):
        base_distance += 1
        current += 1
        if current == the_input:
            return base_distance

    # Left to 0 decreases distance
    for _ in range(half_grid):
        base_distance -= 1
        current += 1
        if current == the_input:
            return base_distance

    # Left beyond 0 increases distance
    for _ in range(half_grid):
        base_distance += 1
        current += 1
        if current == the_input:
            return base_distance

    # Down to 0 decreases distance
    for _ in range(half_grid):
        base_distance -= 1
        current += 1
        if current == the_input:
            return base_distance

    # Down beyond 0 increases distance
    for _ in range(half_grid):
        base_distance += 1
        current += 1
        if current == the_input:
            return base_distance

    # Right to 0 decreases distance
    for _ in range(half_grid):
        base_distance -= 1
        current += 1
        if current == the_input:
            return base_distance

    # Right beyond 0 increases distance
    for _ in range(half_grid):
        base_distance += 1
        current += 1
        if current == the_input:
            return base_distance


def part_two(the_input: int) -> int:
    pass


def main():
    with open('input_03.txt') as f_object:
        input_03 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_03)
    
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
