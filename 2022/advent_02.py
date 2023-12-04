#!/usr/bin/env python3

# Output:
#

def the_setup() -> list:
    the_input = list()
    with open('input_02.txt') as f_object:
        for line in f_object:
            the_input.append(line.strip().split())

    return the_input


def part_one(the_input):
    # A = Rock = X = 1
    # B = Paper = Y = 2
    # C = Scissors = Z = 3

    # elf: (Win, Lose, Draw)
    result_table = {
        'A': ('Y', 'Z', 'X'),
        'B': ('Z', 'X', 'Y'),
        'C': ('X', 'Y', 'Z')
    }
    play_scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    running_sum = 0

    for elf, me in the_input:
        running_sum += play_scores[me]
        if result_table[elf][0] == me: # Win
            running_sum += 6
        elif result_table[elf][1] == me: # Lose
            running_sum += 0
        elif result_table[elf][2] == me: # Draw
            running_sum += 3

    return running_sum


def part_two(the_input):
    # A = Rock = 1
    # B = Paper = 2
    # C = Scissors = 3

    # elf: (Win, Lose, Draw)
    result_table = {
        'A': (6 + 2, 3, 3 + 1),
        'B': (6 + 3, 1, 3 + 2),
        'C': (6 + 1, 2, 3 + 3)
    }

    running_sum = 0

    for elf, me in the_input:
        if me == 'Z':  # Win
            running_sum += result_table[elf][0]
        elif me == 'X':  # Lose
            running_sum += result_table[elf][1]
        elif me == 'Y':  # Draw
            running_sum += result_table[elf][2]

    return running_sum


def main():
    sample_input = """A Y
B X
C Z"""

    # To run against sample input
    # my_input = [i.split() for i in sample_input.split('\n')]

    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
