import re
import time

from helpers import read_file


class Day7:
    def __init__(self) -> None:
        self.name = "Day 7: Bridge Repair"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [3749, 11387]

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

    def can_resolve_to_total(self, result: int, numbers: list[int], part_2=False) -> bool:
        if len(numbers) == 1:
            return numbers[0] == result
        if self.can_resolve_to_total(result, [numbers[0] + numbers[1]] + numbers[2:], part_2):
            return True
        if self.can_resolve_to_total(result, [numbers[0] * numbers[1]] + numbers[2:], part_2):
            return True
        if part_2 and self.can_resolve_to_total(result, [int(f"{numbers[0]}{numbers[1]}")] + numbers[2:], part_2):
            return True
        return False

    def puzzle1(self) -> int:
        total = 0
        for line in self.data:
            result, *numbers = map(int, re.findall(r"\d+", line))
            if self.can_resolve_to_total(result, numbers):
                total += result
        return total

    def puzzle2(self) -> int:
        total = 0
        for line in self.data:
            result, *numbers = map(int, re.findall(r"\d+", line))
            if self.can_resolve_to_total(result, numbers, part_2=True):
                total += result
        return total
