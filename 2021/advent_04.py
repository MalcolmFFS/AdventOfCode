#!/usr/bin/env python3

# Output:
# The final score with the best board (part one) is: 2745.
# The final score with the worst board (part two) is: 6594.


class Board:
    def __init__(self, board: list, board_size: int = 5):
        self.board = board
        self.rows_score = [0 for _ in range(board_size)]
        self.columns_score = [0 for _ in range(board_size)]
        self.marked = list()
        self.unmarked = {
            col: [row_idx, col_idx]
            for row_idx, row in enumerate(self.board)
            for col_idx, col in enumerate(row)
        }

    def calculate_score(self, num: int) -> int:
        return sum(self.unmarked) * num

    def check_for_number(self, num: int) -> int:
        """
        Check if last number called is on board, and score it.
        :param num: Last number called
        :return: 0 for not on baord, 2 if on board but not victory, 1 if victory.
        """
        if num in self.unmarked:
            self.rows_score[self.unmarked[num][0]] += 1
            self.columns_score[self.unmarked[num][1]] += 1
            self.update_marked(num)

            if self.check_victory():
                return True

        else:
            return False

    def check_victory(self) -> bool:
        for i in range(5):
            if self.rows_score[i] == 5 or self.columns_score[i] == 5:
                return True

    def update_marked(self, num: int) -> None:
        del self.unmarked[num]
        self.marked.append(num)

        return

    def __str__(self):
        return '\n'.join([str(row) for row in self.board])


def the_setup() -> tuple:
    with open('input_04.txt') as f_object:
        raw_input = f_object.read().split('\n\n')

    nums = [int(n) for n in raw_input[0].split(',')]
    boards = dict()
    for idx, raw_board in enumerate(raw_input[1:]):
        board = [[int(col) for col in row.split()] for row in raw_board.split('\n')]
        boards[idx] = Board(board, 5)

    return nums, boards


def part_one(nums: list, boards: dict) -> int:
    for num in nums:
        for idx, board in boards.items():
            check_for_num_response = board.check_for_number(num)
            if check_for_num_response:
                continue
            elif check_for_num_response:
                # print(f"\nWinning Board:\n{board}\nMarked Numbers: {board.marked}")
                return board.calculate_score(num)


def part_two(nums: list, boards: dict) -> int:
    for num in nums:
        tmp_boards = boards.copy()
        for idx, board in tmp_boards.items():
            check_for_num_response = board.check_for_number(num)
            if check_for_num_response == 0:
                continue
            elif check_for_num_response == 1:
                if len(boards) == 1:
                    # print(f"\nWinning Board:\n{board}\nMarked Numbers: {board.marked}")
                    return board.calculate_score(num)
                else:
                    del boards[idx]
            elif check_for_num_response == 2:
                continue


def main():
    sample_input = r"""
    Sample input won't work for this setup, would need to hijack the_setup() to use sample input.
    """

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    numbers_called, boards = the_setup()
    print(f"The final score with the winning board (part one) is: {part_one(numbers_called, boards)}.")
    print(f"The final score with the losing board (part two) is: {part_two(numbers_called, boards)}.")


if __name__ == "__main__":
    main()
