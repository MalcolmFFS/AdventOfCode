#!/usr/bin/env python3

# Output:
# 

def the_setup(data: str) -> dict:
    the_input = list()
    for line in data.split('$'):
        the_input.append(line.strip())

    directories = {"/": dict()}
    cur_dir = directories["/"]
    cur_path = [cur_dir]

    for line in the_input[2:]:
        if line.startswith("cd") and ".." not in line:
            directory = str(line.split()[-1])
            cur_dir = cur_dir[directory]
            cur_path.append(cur_dir)

        elif line.startswith("cd") and ".." in line:
            cur_path.pop()
            cur_dir = cur_path[-1]

        elif line.startswith("ls"):
            for i in line.split('\n')[1:]:
                if i.startswith("dir"):
                    directory = i.split()[1]
                    cur_dir[directory] = dict()
                else:
                    file = i.split()[1]
                    size = int(i.split()[0])
                    cur_dir[file] = size

    return directories


def part_one(the_input: dict) -> int:
    running_sum = 0
    for directory, contents in the_input.items():
        if type(contents) == int: # It's a file
            running_sum += contents
            print(f"Added file {directory} size {contents} to running_sum {running_sum}")

        else:  # It's a directory
            dir_size = part_one(contents)
            if dir_size <= 100_000:
                running_sum += dir_size
                print(f"Added directory {directory} size {dir_size} to running_sum {running_sum}")

        if directory == 'a':
            print(f"Running sum on 'a': {running_sum}")

    print(f"Running sum: {running_sum}")
    return running_sum


def part_two(the_input: dict) -> int:
    pass


def main():
    with open('input_08.txt') as f_object:
        input_08 = f_object.read().strip()
    
    # Expected output part 1: 95437 (94853 + 584) (a + e)
    # Expected output part 2: 
    sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    # To run against sample input
    my_input = the_setup(sample_input)

    # To run against real input
    # my_input = the_setup(input_08)

    print(my_input)
    
    print(f"The  (part one) is: {part_one(my_input)}.")
    print(f"The  (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
