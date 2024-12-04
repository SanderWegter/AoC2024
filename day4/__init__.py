import time

from helpers import read_file


class Day4:
    def __init__(self) -> None:
        self.name = "Day 4: Ceres Search"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [18, 9]

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
        target_word = "XMAS"
        directions = [
            (0, 1),  # south
            (1, 0),  # east
            (0, -1),  # north
            (-1, 0),  # west
            (1, 1),  # south-east
            (1, -1),  # south-west
            (-1, 1),  # north-east
            (-1, -1),  # north-west
        ]

        xmas_found = 0
        for y, line in enumerate(self.data):
            for x, letter in enumerate(line):
                if letter == "X":
                    for direction in directions:
                        next_letters = []
                        for index, _ in enumerate(target_word):
                            x_ = x + direction[0] * index
                            y_ = y + direction[1] * index
                            if x_ < 0 or y_ < 0:
                                break
                            try:
                                next_letter = self.data[y_][x_]
                            except IndexError:
                                break
                            next_letters.append(next_letter)
                        if "".join(next_letters) == target_word:
                            xmas_found += 1
                            next_letters = []
        return xmas_found

    def puzzle2(self) -> int:
        xmas_found = 0
        for y, line in enumerate(self.data):
            if y == 0 or y == len(self.data) - 1:
                continue
            for x, letter in enumerate(line):
                if x == 0 or x == len(line) - 1:
                    continue
                if letter == "A":
                    try:
                        lr = self.data[y - 1][x - 1] + self.data[y + 1][x + 1]
                        rl = self.data[y - 1][x + 1] + self.data[y + 1][x - 1]

                        if (
                            (lr == "MS" and rl == "MS")
                            or (lr == "SM" and rl == "SM")
                            or (lr == "MS" and rl == "SM")
                            or (lr == "SM" and rl == "MS")
                        ):
                            xmas_found += 1
                    except IndexError:
                        continue

        return xmas_found
