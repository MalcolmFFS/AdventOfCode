#!/usr/bin/env python3

import re

# Output:
# 

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):
        the_input.append(line)

    return the_input


def part_one(the_input: list) -> int:
    digits = list()
    a, b = 0, 0
    for line in the_input:
        for char in line:
            if char.isdigit():
                a = char
                break
            else:
                pass
        for char in reversed(line):
            if char.isdigit():
                b = char
                break
        digits.append(int(f"{a}{b}"))
    
    return sum(digits)


def part_two(the_input: list) -> int:
    numbers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        "zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]
    replacements = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    digits = list()
    for line in the_input:
        cur_digits = str()
        matches = dict()
        for n in numbers:
            if n in line:
                matches[line.find(n)] = n
                if line.rfind(n) not in matches:
                    matches[line.rfind(n)] = n
        
        a, b = min(matches.keys()), max(matches.keys())
        try:
            if matches[a] in replacements:
                cur_digits += f"{replacements[matches[a]]}"
            else:
                cur_digits += f"{matches[a]}"

            if matches[b] in replacements:
                cur_digits += f"{replacements[matches[b]]}"
            else:
                cur_digits += f"{matches[b]}"
        except KeyError:
            pass

        digits.append(int(cur_digits))

    return sum(digits)


def main():
    with open('input_01.txt') as f_object:
        input_01 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_01)
    
    print(f"The Sum of first and last digits (part one) is: {part_one(my_input[:])}.")
    print(f"The Sum of first and last numbers (part two) is: {part_two(my_input[:])}.")


if __name__ == "__main__":
    main()
    # 
