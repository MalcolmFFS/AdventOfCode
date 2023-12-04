#!/usr/bin/env python


def validate_password_pt1(password):
    prev_digit = None
    double = False

    for digit in str(password)[::-1]:
        digit = int(digit)
        if prev_digit is not None and digit > prev_digit:
            return False
        if prev_digit is not None and digit == prev_digit:
            double = True
        prev_digit = digit

    if double == True:
        return True
    else:
        return False


def validate_password_pt2(password):
    prev_digit = None
    double = {}

    for digit in str(password)[::-1]:
        digit = int(digit)
        if prev_digit is not None and digit > prev_digit:
            return False
        if prev_digit is not None and digit == prev_digit:
            if digit in double:
                double[digit] += 1
            else:
                double[digit] = 1
        prev_digit = digit

    for value in double.values():
        if value > 1:
            continue
        else:
            return True

    return False


if __name__ == "__main__":
    my_input = []

    with open('input_4.txt') as f_object:
        for line in f_object:
            my_input.append(line)

    low_end, high_end = my_input[0].split('-')
    low_end, high_end = int(low_end), int(high_end)

    passwords1 = []
    for i in range(low_end, high_end):
        if validate_password_pt1(i):
            passwords1.append(i)

    passwords1 = set(passwords1)
    print(len(passwords1))

    passwords2 = []
    for i in range(low_end, high_end):
        if validate_password_pt2(i):
            passwords2.append(i)

    passwords2 = set(passwords2)
    print(len(passwords2))

    # print(validate_password(123789))
