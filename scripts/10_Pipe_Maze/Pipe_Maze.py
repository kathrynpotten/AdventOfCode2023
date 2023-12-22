import numpy as np
import math


class Pipe:
    def __init__(self, input_map):
        self.input = input_map
        self.map = input_map.splitlines()
        self.m, self.n = len(self.map), len(self.map[0])
        self.distance_grid = np.full((self.m, self.n), -1)
        self.direction = np.full((self.m, self.n), ".", dtype=str)
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
        row, col = divmod(linear_coord, self.n)
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
        self.direction[self.start_loc] = self.find_direction(move)
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

    def find_direction(self, move):
        if move == (0, 1):
            return "R"
        elif move == (0, -1):
            return "L"
        elif move == (1, 0):
            return "D"
        elif move == (-1, 0):
            return "U"

    def calculate_distances(self):
        self.loop_coords = [self.start_loc]
        current_dist = 0
        self.distance_grid[self.start_loc] = current_dist
        current_loc = self.starting_move()
        previous_loc = self.start_loc

        while current_loc != self.start_loc:
            current_dist += 1
            self.distance_grid[current_loc] = current_dist
            current_loc, move = self.make_move(current_loc, previous_loc)
            previous_loc = tuple(x - y for x, y in zip(current_loc, move))
            self.direction[previous_loc] = self.find_direction(move)
            self.loop_coords.append(current_loc)

        self.loop_length = len(self.loop_coords)
        assert self.loop_length == current_dist + 1

        return self.distance_grid

    def furthest_point(self):
        length_of_loop = self.distance_grid.max()
        return math.ceil(length_of_loop / 2)

    def not_pipe_loop(self):
        non_loop_points = []
        for row in range(self.m):
            for col in range(self.n):
                if self.distance_grid[row][col] == -1:
                    non_loop_points.append((row, col))
        return non_loop_points

    def create_loop_map(self):
        self.loop_map = self.map
        for row in range(self.m):
            for col in range(self.n):
                if self.distance_grid[row][col] == -1:
                    loop_map_row = [pipe for pipe in self.loop_map[row]]
                    loop_map_row[col] = "."
                    self.loop_map[row] = "".join(pipe for pipe in loop_map_row)
        return self.loop_map

    def inside_pipe_loop(self):
        inside_loop = 0
        for row in range(1, self.m - 1):
            up_tally = 0
            down_tally = 0
            for col in range(self.n - 1):
                if self.direction[row][col] == "U":
                    up_tally += 1
                elif self.direction[row][col] == "D":
                    down_tally += 1
                # not quite right...
                elif (
                    self.distance_grid[row][col] == -1
                    and up_tally != down_tally
                    and not (
                        self.distance_grid[row][col:] == [-1] * (self.n - col)
                    ).all()
                    and not (
                        self.distance_grid[row:, :][:, col] == [-1] * (self.m - row)
                    ).all()
                ):
                    inside_loop += 1
                    print(row, col)
        return inside_loop

    def area_of_polygon(self):
        x = [coord[0] for coord in self.loop_coords] + [self.loop_coords[0][0]]
        y = [coord[1] for coord in self.loop_coords] + [self.loop_coords[0][1]]
        S1 = np.sum(x * np.roll(y, -1))
        S2 = np.sum(y * np.roll(x, -1))
        return 0.5 * np.absolute(S1 - S2)

    def points_inside_loop(self):
        area = self.area_of_polygon()
        return int(math.ceil(area) + 1 - (self.loop_length / 2))


if __name__ == "__main__":
    with open("../../input_data/10_Pipe_Maze.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip()

    answer_map = Pipe(input_data)
    answer_map.calculate_distances()
    answer_1 = answer_map.furthest_point()
    print(answer_1)

    answer_2 = answer_map.points_inside_loop()
    print(answer_2)
