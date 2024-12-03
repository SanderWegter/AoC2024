import re
import time

from helpers import read_file


class Day3:
    def __init__(self) -> None:
        self.name = "Day 3: Mull It Over"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [161, 48]

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
        for row in self.data:
            multiplications = re.findall(r"mul\((\d+),(\d+)\)", row)
            result += sum([int(left) * int(right) for left, right in multiplications])
        return result

    def puzzle2(self) -> int:
        result = 0
        is_enabled = True
        for row in self.data:
            row_ops = re.finditer(r"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)", row)
            for op in row_ops:
                if op.group() == "don't()":
                    is_enabled = False
                if op.group() == "do()":
                    is_enabled = True
                if "mul(" in op.group() and is_enabled:
                    multiply = re.findall(r"mul\((\d+),(\d+)\)", op.group())
                    result += int(multiply[0][0]) * int(multiply[0][1])
        return result
