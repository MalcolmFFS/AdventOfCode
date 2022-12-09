#!/usr/bin/env python3

# Output:
# The number of trees visible from outside any row or column (part one) is: 1662.
# The highest scenic score any 1 tree has (part two) is: 537600.

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append(line)

    return the_input


def part_one(the_input: list) -> int:
    visible = list()
    for r_idx, row in enumerate(the_input):
        for c_idx, col in enumerate(row):
            # Get rid of outside trees
            if r_idx == 0 or r_idx == len(the_input) - 1: # len() - 1 because enumerate() starting at 0
                visible.append(col)
                continue

            # Use elif so that it doesn't append pos (0,0) twice
            elif c_idx == 0 or c_idx == len(row) - 1:
                visible.append(col)
                continue

            else:
                # Look up:
                test_r_idx = r_idx - 1
                while test_r_idx >= 0:
                    if col <= the_input[test_r_idx][c_idx]:
                        break
                    test_r_idx -= 1
                else:
                    visible.append(col)
                    continue

                # Look down:
                test_r_idx = r_idx + 1
                while test_r_idx <= len(the_input) - 1:
                    if col <= the_input[test_r_idx][c_idx]:
                        break
                    test_r_idx += 1
                else:
                    visible.append(col)
                    continue

                # Look right:
                test_c_idx = c_idx + 1
                while test_c_idx <= len(row) - 1:
                    if col <= the_input[r_idx][test_c_idx]:
                        break
                    test_c_idx += 1
                else:
                    visible.append(col)
                    continue

                # Look left:
                test_c_idx = c_idx - 1
                while test_c_idx >= 0:
                    if col <= the_input[r_idx][test_c_idx]:
                        break
                    test_c_idx -= 1
                else:
                    visible.append(col)
                    continue

    return len(visible)


def part_two(the_input: list) -> int:
    tree_dict = dict()
    for r_idx, row in enumerate(the_input):
        for c_idx, col in enumerate(row):
            tree_dict[(r_idx, c_idx)] = col

    # Starting score of 0
    scenic_score = 0
    for tree, tree_height in tree_dict.items():
        r_idx, c_idx = tree
        if r_idx == 0 or c_idx == 0:
            continue
        if r_idx == len(the_input) or c_idx == len(the_input[0]):
            break

        # Look up:
        up_scenic_score = 0
        test_r_idx = r_idx - 1
        while test_r_idx >= 0:
            to_test = the_input[test_r_idx][c_idx]
            if tree_height > to_test:
                up_scenic_score += 1
            elif tree_height <= to_test:
                up_scenic_score += 1
                break
            test_r_idx -= 1

        # Look down:
        down_scenic_score = 0
        test_r_idx = r_idx + 1
        while test_r_idx <= len(the_input) - 1:
            to_test = the_input[test_r_idx][c_idx]
            if tree_height > to_test:
                down_scenic_score += 1
            elif tree_height <= to_test:
                down_scenic_score += 1
                break
            test_r_idx += 1

        # Look right:
        right_scenic_score = 0
        test_c_idx = c_idx + 1
        while test_c_idx <= len(row) - 1:
            to_test = the_input[r_idx][test_c_idx]
            if tree_height > to_test:
                right_scenic_score += 1
            elif tree_height <= to_test:
                right_scenic_score += 1
                break
            test_c_idx += 1

        # Look left:
        left_scenic_score = 0
        test_c_idx = c_idx - 1
        while test_c_idx >= 0:
            to_test = the_input[r_idx][test_c_idx]
            if tree_height > to_test:
                left_scenic_score += 1
            elif tree_height <= to_test:
                left_scenic_score += 1
                break
            test_c_idx -= 1

        cur_scenic_score = up_scenic_score * down_scenic_score * right_scenic_score * left_scenic_score
        if cur_scenic_score > scenic_score:
            scenic_score = cur_scenic_score

    return scenic_score


def main():
    with open('input_08.txt') as f_object:
        input_08 = f_object.read().strip()
    
    # Expected output part 1: 21
    # Expected output part 2: 8
    sample_input = """30373
25512
65332
33549
35390"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_08)
    
    print(f"The number of trees visible from outside any row or column (part one) is: {part_one(my_input)}.")
    print(f"The highest scenic score any 1 tree has (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
