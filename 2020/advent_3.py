#!/usr/bin/env python3

## OUCH

# =====Part One:=====
# Going 3 steps right and 1 steps down we hit 159 trees!
#
# =====Part Two:=====
# Going 1 steps right and 1 steps down we hit 86 trees!
# Going 3 steps right and 1 steps down we hit 159 trees!
# Going 5 steps right and 1 steps down we hit 97 trees!
# Going 7 steps right and 1 steps down we hit 88 trees!
# Going 1 steps right and 2 steps down we hit 55 trees!
# The product of the 5 Part Two paths is: 6419669520


def calculate_trees(my_input,steps_right,steps_down):
    column = 0
    row = 0
    trees_hit = 0
    row_len = len(my_input[0])

    while True:
        line = my_input[row].strip()
        pos = column % row_len
        failing = False
        try:
            if line[pos] == "#": trees_hit += 1
        except:
            failing = True
        newline = ""
        line = line.strip()
        if pos > 0 and pos < 31:
            newline += line[0:pos - 1]
            newline += "O"
            newline += line[pos + 1:-1]
            if failing: print(newline, pos, column)
        elif pos == 0:
            newline += "O"
            newline += line[pos + 1:-1]
            if failing: print(newline, pos, column)
        elif pos == 31:
            newline += line[0:pos - 1]
            newline += "O"
            if failing: print(newline, pos, column)
        else:
            newline = "FAILED!!"
            if failing: print(newline, pos, column)

        my_input[row] = newline

        column += steps_right
        row += steps_down
        if row < len(my_input):
            continue
        else:
            break

    output = f'Going {str(steps_right)} steps right and {str(steps_down)} steps down '
    output += f'we hit {str(trees_hit)} trees!'
    return output, trees_hit


my_input = []
with open('input_3.txt') as f_object:
    for line in f_object:
        my_input.append(str(line.strip()))

part_one,part_one_trees = calculate_trees(my_input[:],3,1)
part_two1,part_two1_trees = calculate_trees(my_input[:],1,1)
part_two2,part_two2_trees= calculate_trees(my_input[:],3,1)
part_two3,part_two3_trees= calculate_trees(my_input[:],5,1)
part_two4,part_two4_trees = calculate_trees(my_input[:],7,1)
part_two5,part_two5_trees = calculate_trees(my_input[:],1,2)

part_two_product = part_two1_trees*part_two2_trees*part_two3_trees*part_two4_trees*part_two5_trees


print(f'=====Part One:=====\n{part_one}\n')
print(f'=====Part Two:=====\n{part_two1}')
print(part_two2)
print(part_two3)
print(part_two4)
print(part_two5)
print(f'The product of the 5 Part Two paths is: {part_two_product}')