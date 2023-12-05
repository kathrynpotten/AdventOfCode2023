import re
from collections import Counter


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


class Schematic:
    def __init__(self, input):
        self.input = input
        self.scheme = re.sub(r"[^a-zA-Z0-9 \n\.]", "*", input).splitlines()
        self.symbols = []
        self.adjacent = []
        self.numbers_dict = {}
        self.part_numbers = []
        self.numbers = []

    def __repr__(self):
        return repr(self.input)

    def __str__(self):
        return "\n".join(line for line in self.scheme)

    def position_of_symbols(self):
        for index, line in enumerate(self.scheme):
            symbols_positions = re.finditer(r"\*", line)
            self.symbols.extend([(index, pos.span()[0]) for pos in symbols_positions])

    def adjacency(self):
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
        for symbol in self.symbols:
            adjacenct_positions = [
                tuple(x + y for x, y in zip(symbol, condition))
                for condition in adjacency_conditions
            ]
            self.adjacent.extend(adjacenct_positions)
        self.adjacent.sort()

    def position_of_numbers(self):
        counter = []
        for row_index, line in enumerate(self.scheme):
            digits = re.finditer(r"\d+", line)
            column_indices = []
            for pos in digits:
                repeat = Counter(counter)[int(pos.group())]
                counter.append(int(pos.group()))
                column_indices = [x for x in range(pos.span()[0], pos.span()[1])]
                for column_index in column_indices:
                    self.numbers_dict[(row_index, column_index)] = (
                        int(pos.group()),
                        repeat,
                    )
                    self.numbers.append((int(pos.group()), repeat))
        self.numbers = set(self.numbers)

    def adjacent_numbers(self):
        self.position_of_symbols()
        self.adjacency()
        self.position_of_numbers()
        for number, repeat in self.numbers:
            positions = [
                pos for pos, num in self.numbers_dict.items() if num == (number, repeat)
            ]
            if any(position in self.adjacent for position in positions):
                self.part_numbers.append(number)
        return self.part_numbers

    def sum_engine_parts(self):
        return sum(self.part_numbers)


test_schematic = Schematic(test_data)
test_schematic.adjacent_numbers()
assert test_schematic.sum_engine_parts() == test_result


with open("../input_data/03_Gear_Ratios.txt", "r", encoding="utf-8") as file:
    input = file.read().strip()

answer_schematic = Schematic(input)
answer_schematic.adjacent_numbers()
answer_1 = answer_schematic.sum_engine_parts()
print(answer_1)
