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


if __name__ == "__main__":
    unittest.main()
