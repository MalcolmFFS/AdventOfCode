#!/usr/bin/env python3

# Output:
# The  (part one) is: 245.
# The  (part two) is: 983026.

# advent_08.py
# part_one():
# real    0m0.021s
# part_two()
# real    0m0.024s


def the_setup() -> list:
    the_input = list()
    with open('input_08.txt') as f_object:
        tmp = f_object.read().split('\n')

    for line in tmp:
        the_input.append([[signal for signal in line.split()[:10]],
                         [output for output in line.split()[11:]]]
                         )

    return the_input


def part_one(the_input):
    known_segments = {2: 1, 3: 7, 4: 4, 7: 8}
    counter = 0
    for line in the_input:
        _, outputs = line
        for segment in outputs:
            if len(segment) in known_segments:
                counter += 1

    return counter


def part_two(the_input):
    all_outputs = []
    for line in the_input:
        signals, outputs = line

        intended_mapping = {
            0: 'abcefg',    # 6
            1: 'cf',        # 2
            2: 'acdeg',     # 5
            3: 'acdfg',     # 5
            4: 'bcdf',      # 4
            5: 'abdfg',     # 5
            6: 'abdefg',    # 6
            7: 'acf',       # 3
            8: 'abcdefg',   # 7
            9: 'abcdfg'     # 6
        }
        possibles = dict()  # Keys will be from normal signal, values will be current line
        for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            possibles[x] = list()

        order = [2, 3, 6, 4, 5]
        for i in order:
            for signal in [j for j in signals if len(j) == i]:
                signal = str(signal)
                if len(signal) == 2:  # 1: 'cf'
                    possibles['c'] += signal
                    possibles['f'] += signal

                elif len(signal) == 3:  # 7: 'acf'
                    for char in signal:
                        if char not in possibles['c'] and char not in possibles['f']:
                            possibles['a'] = char

                elif len(signal) == 6:  # 0: 'abcefg', 6: 'abdefg', 9: 'abcdfg'
                    if len(possibles['c']) == 2:
                        x, y = possibles['c']
                        if x not in signal or y not in signal:  # 6: 'abdefg'
                            if x in signal:
                                possibles['c'] = y
                                possibles['f'] = x
                            elif y in signal:
                                possibles['c'] = x
                                possibles['f'] = y
                        elif x in signal and y in signal:  # 0: 'abcefg', 9: 'abcdfg'
                            for key in possibles.keys():
                                if key not in signal:
                                    possibles['d'].append(key)
                                    possibles['e'].append(key)
                    else:
                        for key in possibles.keys():
                            if key not in signal:
                                possibles['d'].append(key)
                                possibles['e'].append(key)

                elif len(signal) == 4:  # 4: 'bcdf'
                    for char in signal:
                        if char != possibles['c'] and char != possibles['f']:
                            if char in possibles['d']:
                                possibles['d'] = char
                                possibles['e'].remove(char)
                                possibles['e'] = str(possibles['e'][0])
                            elif char not in possibles['d']:
                                possibles['b'] = char

                elif len(signal) == 5:  # 2: 'acdeg', 3: 'acdfg', 5: 'abdfg'  ## 3a 1b 2c 3d 1e 2f 3g
                    if possibles['c'] not in signal:  # 5: 'abdfg'
                        for char in signal:
                            if char not in possibles.values():
                                possibles['g'] = char
                    elif possibles['f'] not in signal:  # 2: 'acdeg'
                        for char in signal:
                            if char not in possibles.values():
                                pass
                    else:  # 3: 'acdfg'
                        for char in signal:
                            if char not in possibles.values():
                                possibles['g'] = char

        possibles['d'] = possibles['d'][0]
        possibles['e'] = possibles['e'][0]
        possibles_rev = {v: k for k, v in possibles.items()}  # Keys from current line, values from normal input
        intended_mapping_rev = {v: k for k, v in intended_mapping.items()}
        actual_out = ''
        for output in outputs:
            out = ''
            for char in output:
                out += possibles_rev[char]

            actual_out += str(intended_mapping_rev["".join(sorted(out))])

        all_outputs.append(int(actual_out))

    return sum(all_outputs)


def main():
    sample_input = r"""
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
    """  # pt1: 26; pt2: 61229

    sample_input_2 = r"""
    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
    """

    sample_input_3 = r"""
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
"""

    # To run against sample input
    # my_tmp = sample_input_2.strip().split('\n')
    # samp_input = list()
    # for line in my_tmp:
    #     samp_input.append([[signal for signal in line.split()[:10]],
    #                        [output for output in line.split()[11:]]]
    #                       )
    #
    # print(f"The  (part one) is: {part_one(samp_input)}.")
    # print(f"The  (part two) is: {part_two(samp_input)}.")
    print()
    my_input = the_setup()
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
