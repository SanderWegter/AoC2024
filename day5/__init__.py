import time
from functools import cmp_to_key

from helpers import read_file_grouped


class Day5:
    def __init__(self) -> None:
        self.name = "Day 5: Print Queue"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file_grouped(f"{folder_name}/test.txt")
        self.data_file = read_file_grouped(f"{folder_name}/data.txt")
        self.test_results = [143, 123]

    def results(self) -> dict:
        self.data = self.test_file
        test_1 = "✅" if self.puzzle1() == self.test_results[0] else "⛔️"
        test_2 = "✅" if self.puzzle2() == self.test_results[1] else "⛔️"

        self.data = self.data_file

        start_time = time.time()
        puzzle1 = self.puzzle1()
        p1_time = time.time() - start_time

        start_time = time.time()
        puzzle2 = self.puzzle2()
        p2_time = time.time() - start_time

        return {
            "name": self.name,
            "test1": test_1,
            "test2": test_2,
            "puzzle1": puzzle1,
            "p1_time": p1_time,
            "puzzle2": puzzle2,
            "p2_time": p2_time,
        }

    def puzzle1(self) -> int:
        result = 0
        rules, manual = self.data
        compare = cmp_to_key(lambda x, y: 1 - 2 * (f"{x}|{y}" in rules))
        for pages in manual:
            page_list = pages.split(",")
            if page_list == sorted(page_list, key=compare):
                result += int(page_list[len(page_list) // 2])
        return result

    def puzzle2(self) -> int:
        result = 0
        rules, manual = self.data
        compare = cmp_to_key(lambda x, y: 1 - 2 * (f"{x}|{y}" in rules))
        for pages in manual:
            page_list = pages.split(",")
            sorted_list = sorted(page_list, key=compare)
            if page_list != sorted_list:
                result += int(sorted_list[len(sorted_list) // 2])
        return result
