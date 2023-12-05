import re
from collections import defaultdict


test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_result = 4361
test_result_2 = 467835


class Schematic:
    def __init__(self, input):
        self.input = input
        self.scheme = re.sub(r"[^a-zA-Z0-9 \n\.]", "*", input).splitlines()
        self.symbols = []
        self.gears = []
        self.adjacent = []
        self.adjacent_gears = {}

    def __repr__(self):
        return repr(self.input)

    def __str__(self):
        return "\n".join(line for line in self.scheme)

    def position_of_symbols(self):
        for index, line in enumerate(self.scheme):
            symbols_positions = re.finditer(r"\*", line)
            self.symbols.extend([(index, pos.span()[0]) for pos in symbols_positions])

    def adjacency(self, gears=False):
        adjacency_conditions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
            (-1, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
        ]
        if gears:
            for gear in self.gears:
                adjacenct_positions = [
                    tuple(x + y for x, y in zip(gear, condition))
                    for condition in adjacency_conditions
                ]
                self.adjacent_gears[gear] = sorted(adjacenct_positions)
        else:
            for symbol in self.symbols:
                adjacenct_positions = [
                    tuple(x + y for x, y in zip(symbol, condition))
                    for condition in adjacency_conditions
                ]
                self.adjacent.extend(adjacenct_positions)
            self.adjacent.sort()

    def sum_engine_parts(self):
        self.position_of_symbols()
        self.adjacency()
        sum = 0
        for row_index, line in enumerate(self.scheme):
            digits = re.finditer(r"\d+", line)
            column_indices = []
            for pos in digits:
                column_indices = [x for x in range(pos.span()[0], pos.span()[1])]
                if any(
                    (row_index, col_index) in self.adjacent
                    for col_index in column_indices
                ):
                    sum += int(pos.group())
        return sum

    def position_of_potential_gears(self):
        for index, line in enumerate(self.input.splitlines()):
            gears_positions = re.finditer(r"\*", line)
            self.gears.extend([(index, pos.span()[0]) for pos in gears_positions])

    def sum_of_gear_ratios(self):
        self.position_of_potential_gears()
        self.adjacency(gears=True)
        sum = 0
        for gear in self.gears:
            gear_adjacent = defaultdict(set)
            for x, y in self.adjacent_gears[gear]:
                if self.scheme[x][y].isdigit():
                    digits = re.finditer(r"\d+", self.scheme[x])
                    for digit in digits:
                        column_indices = [
                            x for x in range(digit.span()[0], digit.span()[1])
                        ]
                        if any(col_index == y for col_index in column_indices):
                            gear_adjacent[x].add(int(digit.group()))
            gear_adjacent_list = []
            for item in gear_adjacent.values():
                gear_adjacent_list.extend([val for val in item])
            if len(gear_adjacent_list) == 2:
                prod = 1
                for item in gear_adjacent_list:
                    prod *= item
                sum += prod
        return sum


test_schematic = Schematic(test_data)
assert test_schematic.sum_engine_parts() == test_result
assert test_schematic.sum_of_gear_ratios() == test_result_2


with open("../input_data/03_Gear_Ratios.txt", "r", encoding="utf-8") as file:
    input = file.read().strip()


answer_schematic = Schematic(input)
answer_1 = answer_schematic.sum_engine_parts()
print(answer_1)


answer_2 = answer_schematic.sum_of_gear_ratios()
print(answer_2)
