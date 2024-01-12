import re
import itertools


class Observation:
    def __init__(self, input):
        self.scheme = input.splitlines()
        self.galaxies = {}
        self.galaxy_count = 0

    def __repr__(self):
        return repr(self.scheme)

    def __str__(self):
        return "\n".join(line for line in self.scheme)

    def expand(self):
        expanded_rows = []
        for line in self.scheme:
            if "#" in line:
                expanded_rows.append(line)
            else:
                expanded_rows.append(line)
                expanded_rows.append(line)
        expanded_cols = []
        expanded_rows = list(map(list, zip(*expanded_rows)))
        for line in expanded_rows:
            if "#" in line:
                expanded_cols.append(line)
            else:
                expanded_cols.append(line)
                expanded_cols.append(line)
        expanded_cols = list(map(list, zip(*expanded_cols)))
        expanded = []
        for line in expanded_cols:
            expanded.append("".join(item for item in line))
        self.scheme = expanded
        return self.scheme

    def position_of_galaxies(self):
        for index, line in enumerate(self.scheme):
            galaxies = re.finditer(r"[\#]", line)
            positions = [pos.span()[0] for pos in galaxies]
            for position in positions:
                self.galaxy_count += 1
                self.galaxies[self.galaxy_count] = (index, position)
                self.scheme[index] = "".join(
                    str(self.galaxy_count) if j == position else i
                    for j, i in enumerate(self.scheme[index])
                )
        return self.galaxies, self.galaxy_count

    def galaxy_pairs(self):
        self.pairs = list(itertools.combinations(range(1, self.galaxy_count + 1), 2))
        return self.pairs

    def shortest_path_sum(self):
        self.path_lengths = {}
        for pair in self.pairs:
            start, finish = pair
            start_coord, end_coord = self.galaxies[start], self.galaxies[finish]
            distances = tuple(abs(x - y) for x, y in zip(start_coord, end_coord))
            path_length = distances[0] + distances[1]
            self.path_lengths[pair] = path_length
        return sum(path_length for path_length in self.path_lengths.values())

    def calculate_shortest_paths(self):
        self.expand()
        self.position_of_galaxies()
        self.galaxy_pairs()
        return self.shortest_path_sum()

    def expansion(self):
        expanded_rows = []
        for index, line in enumerate(self.scheme):
            if "#" not in line:
                expanded_rows.append(index)
        expanded_cols = []
        scheme_transpose = list(map(list, zip(*self.scheme)))
        for index, line in enumerate(scheme_transpose):
            if "#" not in line:
                expanded_cols.append(index)
        return expanded_rows, expanded_cols

    def shortest_path_sum_large(
        self, expanded_rows, expanded_cols, expansion_num=1000000
    ):
        self.path_lengths = {}
        for pair in self.pairs:
            start, finish = pair
            start_coord, end_coord = self.galaxies[start], self.galaxies[finish]
            distance_y, distance_x = tuple(
                abs(y - x) for y, x in zip(start_coord, end_coord)
            )
            for coord in range(
                min(start_coord[0], end_coord[0]), max(start_coord[0], end_coord[0])
            ):
                if coord in expanded_rows:
                    distance_y += expansion_num - 1
            for coord in range(
                min(start_coord[1], end_coord[1]), max(start_coord[1], end_coord[1])
            ):
                if coord in expanded_cols:
                    distance_x += expansion_num - 1
            path_length = distance_x + distance_y
            self.path_lengths[pair] = path_length
        return sum(path_length for path_length in self.path_lengths.values())

    def calculate_shortest_paths_large(self, expansion_num=1000000):
        expanded_rows, expanded_cols = self.expansion()
        self.position_of_galaxies()
        self.galaxy_pairs()
        return self.shortest_path_sum_large(expanded_rows, expanded_cols, expansion_num)


if __name__ == "__main__":
    with open(
        "../../input_data/11_Cosmic_Expansion.txt", "r", encoding="utf-8"
    ) as file:
        input_data = file.read().strip()

    answer_obs = Observation(input_data)
    answer_1 = answer_obs.calculate_shortest_paths()
    print(answer_1)

    answer_2 = answer_obs.calculate_shortest_paths_large()
    print(answer_2)

# too high
