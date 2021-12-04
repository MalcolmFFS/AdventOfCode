#!/usr/bin/env python3

# Output:
# The final score with the best board (part one) is: 2745.
# The final score with the worst board (part two) is: 6594.


def the_setup():
    with open('input_04.txt') as f_object:
        tmp = f_object.read().split('\n\n')

    nums = [int(n) for n in tmp[0].split(',')]
    boards = [[[
        [int(col), 0] for col in row.split()]
        for row in board.split('\n')]
        for board in tmp[1:]
    ]

    return nums, boards


def calculate_board_score(board, num):
    unmarked_nums = []
    for my_row in board:
        for my_col in my_row:
            if my_col[1] == 0:
                unmarked_nums.append(my_col[0])

    return sum(unmarked_nums) * num


def part_one(numbers_called, boards):
    for n in numbers_called:
        for board in boards:
            for row in board:
                for col_index, column in enumerate(row):
                    if column[0] == n:
                        column[1] = 1
                        cond1 = sum([col[1] for col in row]) == 5
                        cond2 = sum([row[col_index][1] for row in board]) == 5

                        if cond1 or cond2:
                            return calculate_board_score(board, n)
                    else:
                        continue


def part_two(numbers_called, boards):
    for n in numbers_called:
        tmp_boards = boards[:]

        for board in tmp_boards:
            for row in board:
                for col_index, column in enumerate(row):

                    if column[0] == n:
                        column[1] = 1
                        cond1 = sum([col[1] for col in row]) == 5
                        cond2 = sum([row[col_index][1] for row in board]) == 5

                        if cond1 or cond2:
                            if len(tmp_boards) > 1:
                                boards.remove(board)
                                continue
                            else:
                                return calculate_board_score(board, n)
                    else:
                        continue


def main():
    sample_input = r"""
    Sample input won't work for this setup, would need to hijack the_setup() to use sample input.
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    numbers_called, boards = the_setup()
    print(f"The final score with the best board (part one) is: {part_one(numbers_called, boards)}.")
    print(f"The final score with the worst board (part two) is: {part_two(numbers_called, boards)}.")


if __name__ == "__main__":
    main()
