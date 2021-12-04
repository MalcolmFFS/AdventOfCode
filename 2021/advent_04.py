#!/usr/bin/env python3

# Output:
# The final score with the best board (part one) is: 2745.
# The final score with the worst board (part two) is: 6594.


def the_setup():
    with open('input_04.txt') as f_object:
        tmp = f_object.read().split('\n\n')

    tmp_numbers_called = tmp[0].split(',')
    the_numbers_called = [int(n) for n in tmp_numbers_called]
    the_boards = dict()
    for board_index, board in enumerate(tmp[1:]):
        tmp_board = board.split('\n')
        the_boards[board_index] = list()
        for row in tmp_board:
            the_boards[board_index].append([[int(column), 0] for column in row.split()])

    return the_numbers_called, the_boards


def part_one(the_numbers_called, the_boards):
    def run_game(thy_numbers_called, thy_boards):
        for n in thy_numbers_called:
            for board in thy_boards.values():
                for row in board:
                    for col_index, column in enumerate(row):
                        if column[0] == n:
                            column[1] = 1
                            if sum([col[1] for col in row]) == 5:
                                return board, n
                            if sum([row[col_index][1] for row in board]) == 5:
                                return board, n
                        else:
                            continue

    winning_board, last_num = run_game(the_numbers_called, the_boards)
    unmarked_nums = []
    for my_row in winning_board:
        for my_col in my_row:
            if my_col[1] == 0:
                unmarked_nums.append(my_col[0])

    return sum(unmarked_nums) * last_num


def part_two(the_numbers_called, the_boards):
    def run_game(thy_numbers_called, thy_boards):
        for n in thy_numbers_called:
            tmp_boards = thy_boards.copy()
            for board_index, board in tmp_boards.items():
                for row in board:
                    for col_index, column in enumerate(row):
                        if column[0] == n:
                            column[1] = 1
                            if sum([col[1] for col in row]) == 5:
                                if len(tmp_boards) > 1:
                                    del thy_boards[board_index]
                                    continue
                                else:
                                    return board, n

                            if sum([row[col_index][1] for row in board]) == 5:
                                if len(tmp_boards) > 1:
                                    del thy_boards[board_index]
                                    continue
                                else:
                                    return board, n
                        else:
                            continue

    winning_board, last_num = run_game(the_numbers_called, the_boards)
    unmarked_nums = []
    for my_row in winning_board:
        for my_col in my_row:
            if my_col[1] == 0:
                unmarked_nums.append(my_col[0])

    return sum(unmarked_nums) * last_num


sample_input = r"""
Sample input won't work for this setup, would need to hijack the_setup() to use sample input.
"""


if __name__ == "__main__":
    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    numbers_called, boards = the_setup()
    print(f"The final score with the best board (part one) is: {part_one(numbers_called, boards)}.")
    print(f"The final score with the worst board (part two) is: {part_two(numbers_called, boards)}.")
