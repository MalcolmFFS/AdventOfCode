#!/usr/bin/env python3

# Output:
# The sum of all part numbers in the engine schematic (part one) is: 556057.
# The sum of all gear ratios in the engine schematic (part two) is: 82824352.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append([c for c in line])

    return the_input


def part_one(the_input: list) -> int:
    def track_number(r, c):
        while True:
            if the_input[r][c - 1].isdigit():
                c -= 1
            else:
                break
        
        num_coords = (r, c)
        num = the_input[r][c]
        try:
            while the_input[r][c + 1].isdigit():
                c += 1
                num += the_input[r][c]
        except IndexError:
            pass
        
        return int(num), num_coords

    non_symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    running_sum = 0
    all_n_coords = list()
    for r_idx, row in enumerate(the_input):
        for c_idx, col in enumerate(row):
            if col not in non_symbol: # Is a symbol
                not_top_row = r_idx > 0
                not_bottom_row = r_idx < len(the_input) - 1
                not_left_col = c_idx > 0
                not_right_col = c_idx < len(row) - 1

                if not_top_row and not_left_col: # Top left
                    if the_input[r_idx - 1][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_top_row: # Top middle
                    if the_input[r_idx - 1][c_idx].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_top_row and not_right_col: # Top right
                    if the_input[r_idx - 1][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_left_col: # Middle left
                    if the_input[r_idx][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_right_col: # Middle right
                    if the_input[r_idx][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_bottom_row and not_left_col: # Bottom left
                    if the_input[r_idx + 1][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_bottom_row: # Bottom middle
                    if the_input[r_idx + 1][c_idx].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
                
                if not_bottom_row and not_right_col: # Bottom right
                    if the_input[r_idx + 1][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            running_sum += n
    
    return running_sum


def part_two(the_input: list) -> int:
    def track_number(r, c):
        while True:
            if the_input[r][c - 1].isdigit():
                c -= 1
            else:
                break
        
        num_coords = (r, c)
        num = the_input[r][c]
        try:
            while the_input[r][c + 1].isdigit():
                c += 1
                num += the_input[r][c]
        except IndexError:
            pass
        
        return int(num), num_coords

    running_sum = 0
    all_n_coords = list()
    for r_idx, row in enumerate(the_input):
        for c_idx, col in enumerate(row):
            if col == '*': # Might be gear
                adjacent_nums = 0
                nums = list()
                not_top_row = r_idx > 0
                not_bottom_row = r_idx < len(the_input) - 1
                not_left_col = c_idx > 0
                not_right_col = c_idx < len(row) - 1

                if not_top_row and not_left_col: # Top left
                    if the_input[r_idx - 1][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_top_row: # Top middle
                    if the_input[r_idx - 1][c_idx].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_top_row and not_right_col: # Top right
                    if the_input[r_idx - 1][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx - 1, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_left_col: # Middle left
                    if the_input[r_idx][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_right_col: # Middle right
                    if the_input[r_idx][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_bottom_row and not_left_col: # Bottom left
                    if the_input[r_idx + 1][c_idx - 1].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx - 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_bottom_row: # Bottom middle
                    if the_input[r_idx + 1][c_idx].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if not_bottom_row and not_right_col: # Bottom right
                    if the_input[r_idx + 1][c_idx + 1].isdigit():
                        n, n_coords = track_number(r_idx + 1, c_idx + 1)
                        if n_coords not in all_n_coords:
                            all_n_coords.append(n_coords)
                            adjacent_nums += 1
                            nums.append(n)
                
                if adjacent_nums == 2:
                    running_sum += (nums[0] * nums[1])
    
    return running_sum


def main():
    with open('input_03.txt') as f_object:
        input_03 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_03)
    
    print(f"The sum of all part numbers in the engine schematic (part one) is: {part_one(my_input)}.")
    print(f"The sum of all gear ratios in the engine schematic (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
