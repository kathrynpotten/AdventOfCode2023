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
        return list(itertools.combinations(range(1, self.galaxy_count + 1), 2))
