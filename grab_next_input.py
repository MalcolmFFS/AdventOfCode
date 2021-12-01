#!/usr/bin/env python3


import datetime
import os
import pytz
import requests
import time


def find_time_to_sleep():
    next_release = datetime.datetime.now(pytz.timezone('US/Eastern'))
    next_release += datetime.timedelta(days=1)
    next_release = next_release.replace(hour=0, minute=0, second=1, microsecond=0)
    diff = next_release - datetime.datetime.now(pytz.timezone('US/Eastern'))

    return diff.seconds, next_release.day, next_release.year


def ensure_folder(year):
    year_path = os.path.join(os.getcwd(), year)
    if not os.path.isdir(year_path):
        os.mkdir(year_path)

    return year_path


def get_advent_input(year_path, day, year):
    input_path = os.path.join(year_path, f"input_{day}.txt")
    if not os.path.isfile(input_path):
        url = f"https://adventofcode.com/{year}/day/{day}/input"



if __name__ == "__main__":
    time_to_sleep, a_day, a_year = find_time_to_sleep()
    time.sleep(time_to_sleep)
    cur_path = ensure_folder(a_year)
