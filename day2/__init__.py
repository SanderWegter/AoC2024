import time

from helpers import read_file


class Day2:
    def __init__(self) -> None:
        self.name = "Day 2: Red-Nosed Reports"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [2, 4]

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

    def parsed_input(self) -> list[list[int]]:
        return [[int(x) for x in row.split()] for row in self.data]

    def check_line(self, row: list[int]) -> bool:
        if sorted(row) == row or sorted(row, reverse=True) == row:
            for i in range(len(row) - 1):
                diff = abs(row[i + 1] - row[i])
                if diff > 3 or diff == 0:
                    return False
            else:
                return True
        return False

    def puzzle1(self) -> int:
        safe_reports = 0
        input_data = self.parsed_input()
        for row in input_data:
            if self.check_line(row):
                safe_reports += 1

        return safe_reports

    def puzzle2(self) -> int:
        safe_reports = 0
        input_data = self.parsed_input()
        for row in input_data:
            if self.check_line(row):
                safe_reports += 1
            else:
                for i in range(len(row)):
                    if self.check_line(row[:i] + row[i + 1 :]):
                        safe_reports += 1
                        break
        return safe_reports
