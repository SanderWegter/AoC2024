import datetime
import os

import httpx


def create_folder() -> bool:
    current_day = datetime.date.today().day
    folder_name = f"day{current_day}"
    if not os.path.exists(folder_name):
        os.system(f"cp -r dayX_ {folder_name}")
        return True
    return False


def get_puzzle_input() -> None:
    current_day = datetime.date.today().day
    folder_name = f"day{current_day}"
    with open("cookie.txt") as cookiefile:
        cookie = cookiefile.read().strip()
    url = f"https://adventofcode.com/2024/day/{current_day}/input"
    cookies = {"session": cookie}
    response = httpx.get(url, cookies=cookies)
    if response.status_code == 200:
        with open(f"{folder_name}/data.txt", "w") as file:
            file.write(response.text)


def get_puzzle_name() -> None:
    current_day = datetime.date.today().day
    folder_name = f"day{current_day}"
    url = f"https://adventofcode.com/2024/day/{current_day}"
    response = httpx.get(url)
    if response.status_code == 200:
        for line in response.text.splitlines():
            if f"Day {current_day}:" in line:
                puzzle_name = line.split("--- ")[1].split(" ---")[0]
        with open(f"{folder_name}/__init__.py") as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if "class Day" in line:
                    lines[index] = f"class Day{current_day}:\n"
                if "self.name = " in line:
                    lines[index] = f'        self.name = "{puzzle_name}"\n'
                    break
        with open(f"{folder_name}/__init__.py", "w") as file:
            file.writelines(lines)


if create_folder():
    get_puzzle_name()
    get_puzzle_input()
