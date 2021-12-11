#!/usr/bin/env python3

# Output:
# The score for corruptions found (part one) is: 339411.
# The score for autocompletes found (part two) is: 2289754624.

# advent_10.py
# part_one():
# real    0m0.037s
# part_two()
# real    0m0.029s


def the_setup() -> list:
    the_input = list()
    with open('input_10.txt') as f_object:
        for line in f_object:
            the_input.append([char for char in line.strip()])

    return the_input


def part_one(the_input: list) -> int:
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corruptions = list()

    for line in the_input:
        while True:
            for idx, char in enumerate(line):
                if char in pairs and idx != len(line) - 1:
                    if line[idx + 1] == pairs[char]:
                        line.pop(idx + 1)
                        line.pop(idx)
                        break
            else:
                for unmatched in line:
                    if unmatched in pairs.values():
                        corruptions.append(unmatched)
                        break
                break

    score = 0
    for corruption in corruptions:
        score += scores[corruption]

    return score


def part_two(the_input: list) -> int:
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    incompletes = list()

    for line in the_input:
        while True:
            for idx, char in enumerate(line):
                if char in pairs and idx != len(line) - 1:
                    if line[idx + 1] == pairs[char]:
                        line.pop(idx + 1)
                        line.pop(idx)
                        break
            else:
                for unmatched in line:
                    if unmatched in pairs.keys():
                        continue
                    else:
                        break
                else:
                    incompletes.append(line)
                    break
                break

    line_scores = []
    for line in incompletes:
        line_score = 0
        for unpaired in line[::-1]:
            line_score *= 5
            line_score += scores[pairs[unpaired]]

        line_scores.append(line_score)

    return sorted(line_scores)[(len(line_scores) // 2)]


def main():
    sample_input = r"""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
    """

    # To run against sample input
    # my_input = [[j for j in i] for i in sample_input.strip().split('\n')]
    # for blah in my_input:
    #     print(blah)

    my_input = the_setup()
    print(f"The score for corruptions found (part one) is: {part_one(my_input[:])}.")
    print(f"The score for autocompletes found (part two) is: {part_two(my_input[:])}.")


if __name__ == "__main__":
    main()
