#!/usr/bin/env python3


import os
from datetime import datetime, timedelta


def create_advent_file_with_template(year, day):
    advent_template = f'''#!/usr/bin/env python3

# Output:
# 

def the_setup(data: str) -> list:
    the_input = list()
    for line in data.split('\n'):

        # tmp = f_ob

    return the_input


def part_one(the_input: list) -> int:
    pass


def part_two(the_input: list) -> int:
    pass


def main():
    with open('input_{day}.txt') as f_object:
        input_{day} = f_object.read().strip()
    
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_{day})
    
    print(f"The  (part one) is: {{part_one(my_input)}}.")
    print(f"The  (part two) is: {{part_two(my_input)}}.")


if __name__ == "__main__":
    main()'''

    advent_file_path = f"{year}\\advent_{day}.py"
    if not os.path.exists(advent_file_path):
        print(f"{advent_file_path} doesn't exist, creating...")
        with open(advent_file_path, 'w') as f_object:
            for line in advent_template.splitlines():
                f_object.write(f"{line}\n")
        print(f"{advent_file_path} created successfully!")
    else:
        print(f"{advent_file_path} already exists...")


def create_input_file(year, day):
    input_file_path = f"{year}\\input_{day}.txt"
    if not os.path.exists(f"{input_file_path}"):
        print(f"{input_file_path} doesn't exist, creating...")
        with open(input_file_path, 'w') as _:
            pass
        print(f"{input_file_path} created successfully!")
    else:
        print(f"{input_file_path} already exists...")


if __name__ == "__main__":
    today = datetime.now()
    tomorrow = today + timedelta(1)
    cur_year = tomorrow.year

    if tomorrow.day <= 25:
        print(f"Today is {today.day}, prepping day {tomorrow.day}...")
    else:
        print(f"Tomorrow is {tomorrow.day}, which is above 25. AoC is over. Good bye!")
        exit()

    if not os.path.exists(f"{cur_year}"):
        os.makedirs(f"{cur_year}")
        print(f"Created './{cur_year}/' successfully!")
    else:
        print(f"{cur_year} directory exists...")

    create_advent_file_with_template(cur_year, tomorrow.strftime("%d"))
    create_input_file(cur_year, tomorrow.strftime("%d"))
