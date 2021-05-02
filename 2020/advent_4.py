#!/usr/bin/env python3

def represent_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_hexa(s):
    if s[0] != '#' or len(s) != 7:
        return False
    for char in s[1:].lower():
        if char not in hexa:
            return False
    return True


def format_the_input(my_input):
    formatted = []

    cur_entry = []
    cur_dict = {}
    for line in my_input:
        if line != '':
            for item in line.split():
                cur_entry.append(item)
        elif line == '':
            for item in cur_entry:
                key, value = item.split(':')
                cur_dict.update({key: value})
            formatted.append(cur_dict)
            cur_entry = []
            cur_dict = {}
    return formatted


def do_part_one(formatted):
    valid_count = []
    for person in formatted:
        valid = person.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        if valid:
            valid_count.append(person)
        else:
            continue
    return valid_count


def do_part_two(part_one):
    valid_count = []
    for person in part_one:
        valid = int(person['byr']) >= 1920 and int(person['byr']) <= 2002
        valid &= int(person['iyr']) >= 2010 and int(person['iyr']) <= 2020
        valid &= int(person['eyr']) >= 2020 and int(person['eyr']) <= 2030
        valid &= person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid &= represent_int(person['pid']) and len(person['pid']) == 9
        valid &= is_hexa(person['hcl'])
        if 'in' in person['hgt'][-2:]:
            valid &= int(person['hgt'][:-2]) >= 59 and \
                     int(person['hgt'][:-2]) <= 76
        elif 'cm' in person['hgt'][-2:]:
            valid &= int(person['hgt'][:-2]) >= 150 and \
                 int(person['hgt'][:-2]) <= 193
        else:
            valid &= False

        if valid:
            valid_count.append(person)
        else:
            continue
    return valid_count


my_input = []
with open('input_4.txt') as f_object:
    for line in f_object:
        my_input.append(str(line.strip()))

formatted = format_the_input(my_input)
hexa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

part_one = do_part_one(formatted[:])
part_two = do_part_two(part_one[:])

print(hexa)
print(f'Part one valid: {len(part_one)}')
print(f'Part two valid: {len(part_two)}')