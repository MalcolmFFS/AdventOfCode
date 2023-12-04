#!/usr/bin/env python3

# Output:
# The sum of games possible with 12R, 13G and 14B cubes (part one) is: 2449.
# The power of the minimum possible cubes per game (part two) is: 63981.

def the_setup(data: str) -> dict:
    the_input = dict()
    for line in data.split('\n'):
        game, plays = line.split(":")
        game_plays = list()
        for play in plays.split(';'):
            colors = [0, 0, 0]
            for color in play.split(','):
                if 'red' in color:
                    colors[0] = int(color.split()[0])
                elif 'green' in color:
                    colors[1] = int(color.split()[0])
                elif 'blue' in color:
                    colors[2] = int(color.split()[0])
            game_plays.append(colors)

        the_input[int(game.split()[1])] = game_plays

    return the_input


def part_one(the_input: dict) -> int:
    limit = [12, 13, 14]
    running_sum = 0
    for game in the_input.keys():
        valid = True
        for play in the_input[game]:
            if play[0] > limit[0]:
                valid = False
                break
            if play[1] > limit[1]:
                valid = False
                break
            if play[2] > limit[2]:
                valid = False
                break
        if valid:
            running_sum += game
    
    return running_sum


def part_two(the_input: dict) -> int:
    running_sum = 0
    for game in the_input.keys():
        minimum = [0, 0, 0]
        for play in the_input[game]:
            if play[0] > minimum[0]:
                minimum[0] = play[0]
            if play[1] > minimum[1]:
                minimum[1] = play[1]
            if play[2] > minimum[2]:
                minimum[2] = play[2]
        running_sum += minimum[0] * minimum[1] * minimum[2]
    
    return running_sum


def main():
    with open('input_02.txt') as f_object:
        my_input = f_object.read().strip()

    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(my_input)
    
    print(f"The sum of games possible with 12R, 13G and 14B cubes (part one) is: {part_one(my_input)}.")
    print(f"The power of the minimum possible cubes per game (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
