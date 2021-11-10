#!/usr/bin/env python3

# floor (.)
# an empty seat (L)
# an occupied seat (#)


def the_setup():
    with open('input_11.txt') as f_object:
        the_input = []
        for line in f_object:
            line_list = []
            for char in line.strip():
                line_list.append(char)
            the_input.append(line_list)

    return the_input


def part_one(the_input):
    new_input = []
    for my_row in the_input:
        new_input.append(my_row[:])
    for row_index, my_row in enumerate(the_input):
        for col_index, my_column in enumerate(my_row):
            # print(row_index, col_index)
            adjacents = []
            condition_up = row_index != 0
            condition_left = col_index != 0
            condition_down = row_index != len(the_input) - 1
            condition_right = col_index != len(my_row) - 1

            if condition_up:
                adjacents.append((row_index - 1, col_index))
            if condition_up and condition_right:
                adjacents.append((row_index - 1, col_index + 1))
            if condition_right:
                adjacents.append((row_index, col_index + 1))
            if condition_right and condition_down:
                adjacents.append((row_index + 1, col_index + 1))
            if condition_down:
                adjacents.append((row_index + 1, col_index))
            if condition_down and condition_left:
                adjacents.append((row_index + 1, col_index - 1))
            if condition_left:
                adjacents.append((row_index, col_index - 1))
            if condition_left and condition_up:
                adjacents.append((row_index - 1, col_index - 1))

            # print(f"Adjacents to ({row_index},{col_index}): {adjacents}")

            adjacent_count = 0
            for adjacent in adjacents:
                adj_row, adj_col = adjacent
                # print(f"Checking ({row_index},{col_index}); adjacent {adjacent}; value {the_input[adj_row][adj_col]}")
                if the_input[adj_row][adj_col] == '#':
                    # print(f"Found adjacent occupied!  @ ({adj_row},{adj_col})")
                    # print(f"({row_index},{col_index}): {the_input[row_index][col_index]}")
                    # print(f"Adjacent occupied @ ({adj_row},{adj_col}): {the_input[adj_row][adj_col]}")
                    # print(the_input)
                    adjacent_count += 1
            # print(f"Adjacent count: {adjacent_count}")
            if adjacent_count == 0 and the_input[row_index][col_index] == 'L':
                # print(f"Seat ({row_index},{col_index}) being occupied...")
                new_input[row_index][col_index] = '#'
            elif adjacent_count >= 4 and the_input[row_index][col_index] == '#':
                # print(f"Seat ({row_index},{col_index}) being emptied...")
                new_input[row_index][col_index] = 'L'

    # for my_row in new_input:
    #     print(my_row)
    # print()

    return new_input


if __name__ == "__main__":
    my_input = the_setup()
    shuffle_count = 0
    while True:
        test_shuffle = part_one(my_input[:])
        if test_shuffle == my_input:
            print("They match!")
            print(f"Shuffles: {shuffle_count}")
            break
        else:
            my_input = test_shuffle
            shuffle_count += 1

    occupied_count = 0
    for row in my_input:
        for column in row:
            if column == '#':
                occupied_count += 1

    print(occupied_count)
