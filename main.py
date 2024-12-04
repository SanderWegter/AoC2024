from day1 import Day1
from day2 import Day2
from day3 import Day3
from day4 import Day4

days = [
    Day1(),  # 1722302 / 20373490
    Day2(),  # 564 / 604
    Day3(),  # 174336360 / 88802350
    Day4(),  # 2578 / 1972
]

print(f"╔{'═' * 116}╗")
print(f"║{'Advent of Code 2024'.center(116)}║")
print(f"╠{'═' * 30}╦{'═' * 42}╦{'═' * 42}╣")
print(f"║ {'Name'.center(28)} ║ {'Puzzle 1'.center(40)} ║ {'Puzzle 2'.center(40)} ║")
print(f"╠{'═' * 30}╬{'═'*20}╦{'═'*4}╦{'═'*16}╬{'═'*20}╦{'═'*4}╦{'═'*16}╣")
for day in days:
    result = day.results()  # type: ignore
    result_string = f"║{result['name'].ljust(30)}"
    result_string += f"║{str(result['puzzle1']).center(20)}"
    result_string += f"║ {str(result['test1'])} "
    p1_time = f"{result['p1_time']*1000:0.4f}ms"
    result_string += f"║{str(p1_time).center(16)}"

    result_string += f"║{str(result['puzzle2']).center(20)}"
    result_string += f"║ {str(result['test2'])} "
    p2_time = f"{result['p2_time']*1000:0.4f}ms"
    result_string += f"║{str(p2_time).center(16)}║"

    print(result_string)
print(f"╚{'═' * 30}╩{'═' * 20}╩{'═'*4}╩{'═' * 16}╩{'═' * 20}╩{'═'*4}╩{'═' * 16}╝")
