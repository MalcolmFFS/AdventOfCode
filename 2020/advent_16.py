#!/usr/bin/env python3


from input_16 import valid_fields, nearby_tickets, my_ticket


def part_one(fields, tickets):
    missing = list()
    for ticket in tickets:
        for field in ticket:
            for values in fields.values():
                if field in values:
                    break
                else:
                    continue
            else:
                missing.append(field)

    return sum(missing)


def part_two(fields, tickets, mine):
    for ticket in tickets:
        for field in ticket:
            for values in fields.values():
                if field in values:
                    break
                else:
                    continue
            else:
                tickets.remove(ticket)

    possibles = dict()
    for ticket in tickets:
        for index, field in enumerate(ticket):
            for key, values in fields.items():
                if key not in possibles:
                    possibles[key] = [list(), list()]
                if field in values:
                    if index not in possibles[key][0] and index not in possibles[key][1]:
                        #     if key == 'train':
                        #         print(f"Adding index {index} (value {field}) to key {key}.")
                        possibles[key][0].append(index)
                elif field not in values:
                    if index in possibles[key][0]:
                        #     if key == 'train':
                        #         print(f"Removing index {index} (value {field}) from key {key}.")
                        possibles[key][0].remove(index)
                    if index not in possibles[key][1]:
                        possibles[key][1].append(index)

    done = list()
    done_len = -1
    new_done_len = None
    while len(done) != done_len:
        done_len = new_done_len
        for key, value in sorted(possibles.items(), key=lambda x: len(x[0])):
            # if key == 'arrival location':
            # print(key, value, len(value[0]))
            if len(value[0]) == 1:
                if value[0][0] not in done:
                    # print(value[0])
                    for key2, value2 in possibles.items():
                        if key2 != key and value[0][0] in value2[0]:
                            value2[0].remove(value[0][0])

                    done.append(value[0][0])
                else:
                    pass
                    # print(f"already done {value[0][0]}")

        print(f"[!!] Done: {done}")
        new_done_len = len(done)

    return possibles


if __name__ == "__main__":
    # valid_fields = {
    #     'class': [0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    #     'row': [0,1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19],
    #     'seat': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19]
    # }
    # my_ticket = [11, 12, 13]
    # nearby_tickets = [
    #     [3, 9, 18],
    #     [15, 1, 5],
    #     [5, 14, 9]
    # ]
    print(len(nearby_tickets))
    print(part_one(valid_fields, nearby_tickets[:]))
    part_two_out = part_two(valid_fields, nearby_tickets[:], my_ticket)
    for mykey, myvalue in part_two_out.items():
        print(mykey, myvalue[0])
