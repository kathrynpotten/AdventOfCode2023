import unittest
import Pipe_Maze as pipe
import numpy as np

simple_test_data = """.....
.S-7.
.|.|.
.L-J.
.....""".strip()

simple_test_result = 4

complex_test_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

complex_test_result = 8

simple_test_data_edit = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF""".strip()

part_2_simple_test_data = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".strip()

part_2_simple_test_data_2 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""".strip()

part_2_complex_test_data = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".strip()

part_2_complex_test_data_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".strip()


class Test(unittest.TestCase):
    def test_str(self):
        test_map = pipe.Pipe(simple_test_data)
        result = str(test_map)
        expected_result = ".....\n.S-7.\n.|.|.\n.L-J.\n....."
        self.assertEqual(result, expected_result)

    def test_distance_grid(self):
        test_map = pipe.Pipe(simple_test_data)
        result = np.shape(test_map.distance_grid)
        expected_result = (5, 5)
        self.assertEqual(result, expected_result)

    def test_starting_loc(self):
        test_map = pipe.Pipe(simple_test_data)
        result = test_map.starting_loc()
        expected_result = (1, 1)
        self.assertEqual(result, expected_result)

    def test_starting_direction(self):
        test_map = pipe.Pipe(simple_test_data)
        result = test_map.starting_move()
        expected_result = tuple(x + y for x, y in zip(test_map.start_loc, (0, 1)))
        self.assertEqual(result, expected_result)

    def test_simple_loop(self):
        test_map = pipe.Pipe(simple_test_data)
        result = test_map.calculate_distances()
        expected_result = np.array(
            [
                [-1, -1, -1, -1, -1],
                [-1, 0, 1, 2, -1],
                [-1, 7, -1, 3, -1],
                [-1, 6, 5, 4, -1],
                [-1, -1, -1, -1, -1],
            ]
        )
        self.assertEqual(result.all(), expected_result.all())

    """def test_direction(self):
        test_map = pipe.Pipe(simple_test_data)
        test_map.calculate_distances()
        result = test_map.direction
        expected_result = np.array(
            [
                [".", ".", ".", ".", "."],
                [".", "R", "R", "D", "."],
                [".", "U", ".", "D", "."],
                [".", "U", "L", "L", "."],
                [".", ".", ".", ".", "."],
            ]
        )
        self.assertEqual(result.all(), expected_result.all())"""

    def test_simple_result(self):
        test_map = pipe.Pipe(simple_test_data)
        test_map.calculate_distances()
        result = test_map.furthest_point()
        expected_result = simple_test_result
        self.assertEqual(result, expected_result)

    def test_complex_result(self):
        test_map = pipe.Pipe(complex_test_data)
        test_map.calculate_distances()
        result = test_map.furthest_point()
        expected_result = complex_test_result
        self.assertEqual(result, expected_result)

    def test_non_loop(self):
        test_map = pipe.Pipe(simple_test_data)
        test_map.calculate_distances()
        result = len(test_map.not_pipe_loop())
        expected_result = 17
        self.assertEqual(result, expected_result)

    def test_loop_map(self):
        test_map = pipe.Pipe(simple_test_data_edit)
        test_map.calculate_distances()
        result = test_map.create_loop_map()
        expected_result = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]
        self.assertEqual(result, expected_result)

    def test_inside_loop_area(self):
        test_map_1 = pipe.Pipe(part_2_simple_test_data)
        test_map_1.calculate_distances()
        result_1 = test_map_1.points_inside_loop()
        expected_result_1 = 4
        test_map_2 = pipe.Pipe(part_2_simple_test_data_2)
        test_map_2.calculate_distances()
        result_2 = test_map_2.points_inside_loop()
        expected_result_2 = 4
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))

    """def test_inside_loop_area_complex(self):
        test_map_1 = pipe.Pipe(part_2_complex_test_data)
        test_map_1.calculate_distances()
        result_1 = test_map_1.points_inside_loop()
        expected_result_1 = 8
        test_map_2 = pipe.Pipe(part_2_complex_test_data_2)
        test_map_2.calculate_distances()
        result_2 = test_map_2.points_inside_loop()
        expected_result_2 = 10
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))"""

    def test_inside_loop(self):
        test_map_1 = pipe.Pipe(part_2_simple_test_data)
        test_map_1.calculate_distances()
        result_1 = test_map_1.inside_pipe_loop()
        expected_result_1 = 4
        test_map_2 = pipe.Pipe(part_2_simple_test_data_2)
        test_map_2.calculate_distances()
        result_2 = test_map_2.inside_pipe_loop()
        expected_result_2 = 4
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))

    def test_inside_loop_complex(self):
        test_map_1 = pipe.Pipe(part_2_complex_test_data)
        test_map_1.calculate_distances()
        print("complex1")
        result_1 = test_map_1.inside_pipe_loop()
        expected_result_1 = 8
        test_map_2 = pipe.Pipe(part_2_complex_test_data_2)
        test_map_2.calculate_distances()
        print("complex2")
        result_2 = test_map_2.inside_pipe_loop()
        expected_result_2 = 10
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))


if __name__ == "__main__":
    unittest.main()
