import time
from collections import Counter

from helpers import read_file


class Day1:
    def __init__(self) -> None:
        self.name = "Day 1: Historian Hysteria"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [11, 31]

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

    def parsed_lists(self) -> tuple[list[int], list[int]]:
        left_list = []
        right_list = []
        for line in self.data:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list

    def puzzle1(self) -> int:
        left_list, right_list = self.parsed_lists()
        left_list.sort()
        right_list.sort()
        return sum([abs(left - right) for left, right in zip(left_list, right_list, strict=False)])

    def puzzle2(self) -> int:
        left_list, right_list = self.parsed_lists()
        right_count = Counter(right_list)
        return sum(left * right_count[left] for left, right in zip(left_list, right_list, strict=False))
