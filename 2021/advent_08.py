#!/usr/bin/env python3

# Output:
#


from collections import defaultdict


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
    known_segments = {2: 1, 3: 7, 4: 4, 7: 8}  # length of signal, number it represents
    intended_mapping = {
        0: 'abcefg',   # 6
        1: 'cf',       # 2
        2: 'acdeg',    # 5 -> contains none
        3: 'acdfg',    # 5
        4: 'bcdf',     # 4
        5: 'abdfg',    # 5 -> contains none
        6: 'abdefg',   # 6 -> contains none
        7: 'acf',      # 3
        8: 'abcdefg',  # 7
        9: 'abcdf'     # 5
    }
    possible_mappings = {
        7: {5: [3, 9], 6: [0]},
        4: {5: [9], 6: []},
    }
    all_outputs = list()
    for line in the_input:
        cur_mapping = defaultdict(list)
        signals, outputs = line
        for signal in signals:
            if len(signal) in known_segments:
                cur_mapping[known_segments[len(signal)]].append(signal)
        for output in outputs:
            if len(output) in known_segments:
                cur_mapping[known_segments[len(output)]].append(output)

        for signal in signals:
            if len(signal) in known_segments:
                continue
            for char in cur_mapping[1][0]:
                if char not in signal:
                    cur_mapping[6].append(signal)
                    break
            else:
                for char in cur_mapping[7][0]:
                    if char not in signal:
                        if len(signal) == 5:
                            cur_mapping[2].append(signal)
                        break
                else:
                    for char in cur_mapping[4][0]:
                        if char not in signal:
                            if len(signal) == 5:
                                cur_mapping[3].append(signal)
                                break
                            elif len(signal) == 6:
                                cur_mapping[0].append(signal)
                                break
                    else:
                        cur_mapping[9].append(signal)

        cur_output = ''
        # print(cur_mapping)
        # print(outputs)
        for output in outputs:
            found_flag = False
            # print(f"Working on output: {output}!")
            if len(output) in known_segments:
                cur_output += str(known_segments[len(output)])
                # print(f"{output} has len() {len(output)} which is in known_segments, adding '{known_segments[len(output)]}'")
                found_flag = True
                continue

            if len(output) == 6:
                cur_valid = '6'
            elif len(output) == 5:
                c = [x for x in cur_mapping[1][0] if x not in cur_mapping[6][0]]
                if c[0] in output:
                    cur_valid = '2'
                else:
                    cur_valid = '5'
            for key, value in known_segments.items():
                for char in cur_mapping[value][0]:
                    if char not in output:
                        # print(f"{output} was excluded by {value} ({cur_mapping[value][0]}), adding previously valid '{cur_valid}'")
                        if cur_valid != '6' and cur_valid != '5' and cur_valid != '2':
                            if previous_value == 7:
                                if len(output) == 6:
                                    cur_valid = '0'
                                elif len(output) == 5:
                                    cur_valid = '3'
                            elif previous_value == 4:
                                cur_valid = '9'

                            # possible_mappings
                            # 7: {5: [3, 9], 6: [0]},
                            # 4: {5: [9], 6: []},

                        cur_output += str(cur_valid[0])
                        found_flag = True
                        break
                else:
                    # print(f"{output} was not excluded by {value}")
                    previous_value = value
                    cur_valid = str(value)
                    continue
                if found_flag:
                    break

        # print(cur_output)
        print(cur_mapping)
        print(signals, outputs, cur_output)
        all_outputs.append(int(cur_output))

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
    """

    sample_input_2 = r"""
    acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
    """

    # To run against sample input
    my_tmp = sample_input_2.strip().split('\n')
    samp_input = list()
    for line in my_tmp:
        samp_input.append([[signal for signal in line.split()[:10]],
                           [output for output in line.split()[11:]]]
                          )

    print(f"The  (part one) is: {part_one(samp_input)}.")
    print(f"The  (part two) is: {part_two(samp_input)}.")
    print()
    # my_input = the_setup()
    # print(f"The  (part one) is: {part_one(my_input)}.")
    # print(f"The  (part two) is: {part_two(my_input)}.")
    # (You guessed 983593.) ## too high


if __name__ == "__main__":
    main()
