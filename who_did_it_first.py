#!/usr/bin/env python3


import datetime
import json
import requests
from login_info import aoc_cookie


def choose_leaderboard():
    leaderboards = {
        'malcolm': 997643,
        'tanner': 299981
    }

    print("Private Leaderboards available:")
    for the_owner in leaderboards.keys():
        print(f"\t- {the_owner.title()}")

    while True:
        owner_to_check = input("What private leaderboard should I check?\n ->")
        if owner_to_check.lower() not in leaderboards.keys():
            print("Try again, value not accepted...")
            continue
        else:
            print(f"Checking {owner_to_check.title()}'s leaderboard...")
            return leaderboards[owner_to_check.lower()], owner_to_check


def get_leaderbord_json(year_to_check, owner_to_check):
    leaderboard_url = f"https://adventofcode.com/{year_to_check}/leaderboard/private/view/{owner_to_check}.json"

    response = requests.get(
        leaderboard_url,
        cookies={'session': aoc_cookie},
        headers={"User-Agent": "MalcolmFFS leaderboard checker"}
    )
    response.raise_for_status()
    the_json = json.loads(response.text)

    return the_json


def get_year_input():
    cur_year = datetime.datetime.now().year
    previous_years = [i for i in range(2015, cur_year + 1)]

    print("Years available:")
    for previous_year in previous_years:
        print(f"\t- {previous_year}")

    while True:
        year_to_check = int(input("What year should I get the leaderboard for?\n ->"))
        if year_to_check not in previous_years:
            print("Try again, value not accepted...")
            continue
        else:
            print(f"Checking year {year_to_check}...")
            return year_to_check


def print_leaderboard(the_year, the_owner, the_leaderboard):
    now = datetime.datetime.now()
    if now.hour >= 22 and the_year == now.year:
        cur_day = now.day + 1
    elif the_year != now.year:
        cur_day = 25
    else:
        cur_day = now.day

    exercises = dict()
    # members = dict()
    for user_id in the_leaderboard['members'].keys():
        user_name = the_leaderboard['members'][user_id]['name']
        if user_name is None:
            user_name = user_id

        try:
            for day in range(1, cur_day + 1):
                try:
                    _ = exercises[day][1]
                except KeyError:
                    exercises[day] = {1: list(),
                                      2: list()}
                for part in exercises[day]:
                    # Uhm... yeah... it's long... what about it?
                    completion_time = the_leaderboard['members'][user_id]['completion_day_level'][str(day)][str(part)]['get_star_ts']
                    converted_time = datetime.datetime.fromtimestamp(completion_time)
                    exercises[day][part].append(
                        (user_name, converted_time)
                    )
        except KeyError:
            pass

    # print(members)
    # print(exercises)
    print(f"{the_owner.title()}'s Private Leaderboard:")
    for day, parts in exercises.items():
        for part, part_leaderboard in parts.items():
            print(f"Day {day}, Part {part}:")
            for index, completer in enumerate(sorted(part_leaderboard, key=lambda x: x[1]), start=1):
                print(f"{index} -> {completer[0]} ({completer[1]})")


if __name__ == "__main__":
    year = get_year_input()
    owner_id, owner = choose_leaderboard()
    leaderboard = get_leaderbord_json(year, owner_id)

    print_leaderboard(year, owner, leaderboard)
