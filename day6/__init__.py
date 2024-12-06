import time

from helpers import read_file


class Day6:
    def __init__(self) -> None:
        self.name = "Day 6: Guard Gallivant"
        folder_name = self.__class__.__name__.lower()
        self.test_file = read_file(f"{folder_name}/test.txt")
        self.data_file = read_file(f"{folder_name}/data.txt")
        self.test_results = [41, 6]

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

    def walk(self, guard_location: tuple[int, int], data: list) -> tuple[set, bool]:
        visited_locations = set()
        looped_locations = set()
        is_looped = False
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        current_direction = 0

        while True:
            next_location = (
                guard_location[0] + directions[current_direction][0],
                guard_location[1] + directions[current_direction][1],
            )
            if (
                next_location[0] < 0
                or next_location[0] >= len(data[0])
                or next_location[1] < 0
                or next_location[1] >= len(data)
            ):
                break
            if (next_location, current_direction) in looped_locations:
                is_looped = True
                break
            if data[next_location[1]][next_location[0]] == "." or data[next_location[1]][next_location[0]] == "^":
                guard_location = next_location
                visited_locations.add(guard_location)
                looped_locations.add((guard_location, current_direction))
            if data[next_location[1]][next_location[0]] == "#":
                current_direction = (current_direction + 1) % 4
        return visited_locations, is_looped

    def puzzle1(self) -> int:
        for y, index in enumerate(self.data):
            for x, value in enumerate(index):
                if value == "^":
                    guard_location = (x, y)
        return len(self.walk(guard_location, self.data)[0])

    def puzzle2(self) -> int:
        possibilities = 0
        for y, index in enumerate(self.data):
            for x, value in enumerate(index):
                if value == "^":
                    guard_location = (x, y)
        first_walk = self.walk(guard_location, self.data)[0]

        for coord in first_walk:
            new_data = self.data.copy()
            new_data[coord[1]] = new_data[coord[1]][: coord[0]] + "#" + new_data[coord[1]][coord[0] + 1 :]
            if self.walk(guard_location, new_data)[1]:
                possibilities += 1
        return possibilities
