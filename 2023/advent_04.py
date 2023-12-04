#!/usr/bin/env python3

# Output:
# The total number of points on the cards (part one) is: 25231.
# The total number of cards (part two) is: 9721255.

def the_setup(data: str) -> dict:
    the_input = dict()
    for line in data.split('\n'):
        card_num = int(line.split(':')[0].split()[1])
        winning_nums = line.split(':')[1].split('|')[0]
        my_nums = line.split(':')[1].split('|')[1]
        the_input[card_num] = list()
        the_input[card_num].append([int(n) for n in winning_nums.split()])
        the_input[card_num].append([int(n) for n in my_nums.split()])

    return the_input


def part_one(the_input: dict) -> int:
    total_points = 0
    for card in the_input:
        winning, mine = the_input[card]
        card_points = 0
        for n in mine:
            if n in winning and card_points > 0:
                card_points *= 2
            elif n in winning and card_points == 0:
                card_points = 1
        total_points += card_points

    return total_points


def part_two(the_input: dict) -> int:
    def add_cards(the_card):
        for x in cards_added[the_card]:
            total_cards.append(x)
            add_cards(x)

    processed = [card for card in the_input]

    cards_added = dict()
    while len(processed) > 0:
        cur_card = processed[0]

        cards_added[cur_card] = list()
        winning, mine = the_input[cur_card]
        card_wins = 0

        for n in mine:
            if n in winning:
                card_wins += 1

        for i in range(cur_card + 1, cur_card + 1 + card_wins):
            cards_added[cur_card].append(i)

        processed.remove(cur_card)

    total_cards = list()
    for card in the_input:
        total_cards.append(card)
        add_cards(card)

    return len(total_cards)


def main():
    with open('input_04.txt') as f_object:
        input_04 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_04)
    
    print(f"The total number of points on the cards (part one) is: {part_one(my_input)}.")
    print(f"The total number of cards (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
