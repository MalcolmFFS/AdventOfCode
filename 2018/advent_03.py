#!/usr/bin/env python3

# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge,
# 2 inches from the top edge, 5 inches wide, and 4 inches tall.

# Output:
# The number of square inches that are in at least 2 claims (part one) is: 110827.
# The only claim ID with 0 overlaps (part two) is: 116.

def the_setup(data: str) -> dict:
    # #123 @ 3,2: 5x4
    the_input = dict()
    for line in data.split('\n'):
        cut_id, _, from_corner, dimensions = line[1:].split() # ['123', '@', '3,2:', '5x4']
        from_left, from_top = from_corner[:-1].split(',') # ['3', '2']
        the_input[int(cut_id)] = {
            "from_top": int(from_top),
            "from_left": int(from_left),
            "width": int(dimensions.split('x')[0]),
            "height": int(dimensions.split('x')[1]),
            "overlapped": False
        }

    return the_input


def measure(the_input: dict) -> tuple:
    widths = list()
    heights = list()
    for _, measurements in the_input.items():
        widths.append(measurements["from_left"] + measurements["width"])
        heights.append(measurements["from_top"] + measurements["height"])

    return max(widths), max(heights)


def map_original_fabric(size: tuple) -> list[list]:
    max_width, max_height = size
    original_fabric = list()
    for i in range(max_height):
        original_fabric.append(list())
        for _ in range(max_width):
            original_fabric[i].append('.')

    return original_fabric


def part_one(the_input: dict) -> int:
    full_fabric_measurements = measure(the_input)
    original_fabric = map_original_fabric(full_fabric_measurements)

    for claim_id, measurements in the_input.items():
        for i in range(measurements["from_top"], measurements["height"] + measurements["from_top"]):
            for j in range(measurements["from_left"], measurements["width"] + measurements["from_left"]):
                if original_fabric[i][j] == '.':
                    original_fabric[i][j] = claim_id
                else:
                    original_fabric[i][j] = 'x'

    count = 0
    for i in original_fabric:
        for j in i:
            if j == 'x':
                count += 1

    return count

def part_two(the_input: dict) -> int:
    full_fabric_measurements = measure(the_input)
    original_fabric = map_original_fabric(full_fabric_measurements)

    for claim_id, measurements in the_input.items():
        for i in range(measurements["from_top"], measurements["height"] + measurements["from_top"]):
            for j in range(measurements["from_left"], measurements["width"] + measurements["from_left"]):
                if original_fabric[i][j] == '.':
                    original_fabric[i][j] = claim_id
                elif isinstance(original_fabric[i][j], int):
                    original_fabric[i][j] = 'x'
                    the_input[claim_id]["overlapped"] = True

    for claim_id, measurements in the_input.items():
        for i in range(measurements["from_top"], measurements["height"] + measurements["from_top"]):
            for j in range(measurements["from_left"], measurements["width"] + measurements["from_left"]):
                if original_fabric[i][j] == 'x':
                    the_input[claim_id]["overlapped"] = True

    for claim_id in the_input.keys():
        if not the_input[claim_id]["overlapped"]:
            intact_claim = claim_id

    return intact_claim


def main():
    with open('input_03.txt') as f_object:
        input_03 = f_object.read().strip()
    
    # Expected output part 1: 
    # Expected output part 2: 
    sample_input = """"""

    # To run against sample input
    # my_input = the_setup(sample_input)

    # To run against real input
    my_input = the_setup(input_03)
    
    print(f"The number of square inches that are in at least 2 claims (part one) is: {part_one(my_input)}.")
    print(f"The only claim ID with 0 overlaps (part two) is: {part_two(my_input)}.")


if __name__ == "__main__":
    main()
