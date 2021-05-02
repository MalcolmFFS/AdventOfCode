#!/usr/bin/env python3


def recurse_for_bags(result,organized,goal_bag='shiny gold'):
    result = []
    for line in organized:
        for dict in line[1:]:
            for value in dict.values():
                if goal_bag in value:
                    result.append(line[0])
                    for bag in recurse_for_bags(result,organized,line[0]):
                        result.append(bag)

    return set(result)


def recurse_for_count(organized,goal_bag='shiny gold'):
    count = 0
    for line in organized:
        if line[0] == goal_bag:
            for dict in line[1:]:
                for key,value in dict.items():
                    if key != 'no':
                        bag_count = int(key)
                        # I honestly don't really get how this works, fiddled until it did
                        count += bag_count + bag_count * recurse_for_count(organized,value)
                    elif key == 'no':
                        return 0
    return count


def organize_input(my_input):
    organized = []
    for line in my_input:
        cur_entry = []
        my_split = line.split(',')
        tmp = my_split[0].split()[0]
        tmp += f' {my_split[0].split()[1]}'
        cur_entry.append(tmp)
        tmp = {
            my_split[0].split()[4]: my_split[0].split()[5] + ' ' +
                                    my_split[0].split()[6]
        }
        cur_entry.append(tmp)
        try:
            for your_split in my_split[1:]:
                tmp = {your_split.split()[0]: your_split.split()[1] + ' ' +
                                              your_split.split()[2]
                       }
                cur_entry.append(tmp)
        except IndexError:
            print("This line had no comma.")
        organized.append(cur_entry)

    return organized


if __name__ == "__main__":
    with open('input_7.txt') as f_object:
        my_input = f_object.read().split('\n')

    organized = organize_input(my_input[:])

    answer = recurse_for_bags([],organized,)
    print(f'Part one answer: {len(answer)}')

    answer_2 = recurse_for_count(organized,goal_bag='shiny gold')
    print(f'Part two answer: {answer_2}')

