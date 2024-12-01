def read_file(input_file: str = "") -> list[str]:
    with open(input_file) as f:
        return [line.rstrip("\n") for line in f.readlines()]


def read_file_grouped(input_file: str = "") -> list[list[str]]:
    with open(input_file) as f:
        file_data = f.read().split("\n\n")
        return [line.split("\n") for line in file_data]
