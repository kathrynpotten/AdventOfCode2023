import numpy as np
import math


class Pipe:
    def __init__(self, input_map):
        self.input = input_map
        self.map = input_map.splitlines()
        self.m, self.n = len(self.map[0]), len(self.map)
        self.distance_grid = np.full((self.m, self.n), -1)
        self.start_loc = None
        self.starting_loc()
        self.pipes = ["|", "-", "L", "J", "7", "F"]
        self.loop_dict = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
        }

    def __str__(self):
        return "\n".join(line for line in self.map)

    def starting_loc(self):
        linear_coord = self.input.replace("\n", "").index("S")
        row, col = divmod(linear_coord, self.m)
        self.start_loc = (row, col)
        return self.start_loc

    def starting_move(self):
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in possible_moves:
            row, col = tuple(x + y for x, y in zip(self.start_loc, move))
            current_pipe = self.map[row][col]
            opposite_move = (move[0] * -1, move[1] * -1)
            if current_pipe == ".":
                continue
            elif opposite_move in self.loop_dict[current_pipe]:
                current_loc = (row, col)
                break
        return current_loc

    def possible_move(self, current_loc, previous_loc, possible_moves):
        for move in possible_moves:
            row, col = tuple(x + y for x, y in zip(current_loc, move))
            current_pipe = self.map[row][col]
            opposite_move = (move[0] * -1, move[1] * -1)
            if current_pipe == ".":
                continue
            elif current_pipe == "S":
                current_loc = (row, col)
                break
            elif tuple(x + y for x, y in zip(current_loc, move)) == previous_loc:
                continue
            elif opposite_move in self.loop_dict[current_pipe]:
                current_loc = (row, col)
                break
        return current_loc, move

    def make_move(self, current_loc, previous_loc):
        row, col = current_loc
        current_pipe = self.map[row][col]
        possible_moves = self.loop_dict[current_pipe]
        current_loc, move = self.possible_move(
            current_loc, previous_loc, possible_moves
        )
        return current_loc, move

    def calculate_distances(self):
        current_dist = 0
        self.distance_grid[self.start_loc] = current_dist
        current_loc = self.starting_move()
        previous_loc = self.start_loc

        while current_loc != self.start_loc:
            current_dist += 1
            self.distance_grid[current_loc] = current_dist
            current_loc, move = self.make_move(current_loc, previous_loc)
            previous_loc = tuple(x - y for x, y in zip(current_loc, move))

        return self.distance_grid

    def furthest_point(self):
        length_of_loop = self.distance_grid.max()
        return math.ceil(length_of_loop / 2)


if __name__ == "__main__":
    with open("../../input_data/10_Pipe_Maze.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip()

    answer_map = Pipe(input_data)
    answer_map.calculate_distances()
    answer_1 = answer_map.furthest_point()
    print(answer_1)
