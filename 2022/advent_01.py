#!/usr/bin/env python3

# Output:
#


def the_setup() -> dict:
    # the_input = list()
    with open('input_01.txt') as f_object:
        the_input = f_object.read()

    food_dict = dict()
    for elf, elf_food in enumerate(the_input.split('\n\n')):
        food_dict[elf] = [int(food) for food in elf_food.split('\n')]

    return food_dict


def part_one(the_input):
    return max(sum(elf_food) for elf_food in the_input.values())


def part_two(the_input):
    highest = list()

    all_elves_max = [sum(elf_food) for elf_food in the_input.values()]

    highest.append(max(all_elves_max))
    all_elves_max.remove(max(all_elves_max))
    highest.append(max(all_elves_max))
    all_elves_max.remove(max(all_elves_max))
    highest.append(max(all_elves_max))
    all_elves_max.remove(max(all_elves_max))

    return sum(highest)


def main():
    #     sample_input = """1000
    # 2000
    # 3000
    #
    # 4000
    #
    # 5000
    # 6000
    #
    # 7000
    # 8000
    # 9000
    #
    # 10000"""

    # To run against sample input
    # my_input = [i for i in sample_input.strip().split('\n')]

    my_input = the_setup()
    print(f"The most calories carried by a single elf (part one) is: {part_one(my_input)}.")
    print(f"The top 3 elves together total calories (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
