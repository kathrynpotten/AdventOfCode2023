import unittest
import Cosmic_Expansion as cosmic
import numpy as np

test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".strip()

test_data_expanded = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""

test_result = 374


class Test(unittest.TestCase):
    def test_str(self):
        test_map = cosmic.Observation(test_data)
        result = str(test_map)
        expected_result = "...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#....."
        self.assertEqual(result, expected_result)

    def test_expansion(self):
        test_map = cosmic.Observation(test_data)
        test_map.expand()
        result = str(test_map)
        expected_result = "....#........\n.........#...\n#............\n.............\n.............\n........#....\n.#...........\n............#\n.............\n.............\n.........#...\n#....#......."
        self.assertEqual(result, expected_result)

    def test_position_of_galaxies(self):
        test_observation = cosmic.Observation(test_data)
        test_observation.expand()
        result = test_observation.position_of_galaxies()[0]
        expected_result = {
            1: (0, 4),
            2: (1, 9),
            3: (2, 0),
            4: (5, 8),
            5: (6, 1),
            6: (7, 12),
            7: (10, 9),
            8: (11, 0),
            9: (11, 5),
        }
        self.assertEqual(result, expected_result)

    def test_galaxy_update(self):
        test_observation = cosmic.Observation(test_data)
        test_observation.expand()
        test_observation.position_of_galaxies()
        result = str(test_observation)
        expected_result = "....1........\n.........2...\n3............\n.............\n.............\n........4....\n.5...........\n............6\n.............\n.............\n.........7...\n8....9......."
        self.assertEqual(result, expected_result)

    def test_galaxy_pairs(self):
        test_observation = cosmic.Observation(test_data)
        test_observation.expand()
        test_observation.position_of_galaxies()
        result = len(test_observation.galaxy_pairs())
        expected_result = 36
        self.assertEqual(result, expected_result)

    def test_path_lengths(self):
        test_observation = cosmic.Observation(test_data)
        test_observation.expand()
        test_observation.position_of_galaxies()
        test_observation.galaxy_pairs()
        result = test_observation.shortest_path_sum()
        expected_result = test_result
        self.assertEqual(result, expected_result)

    def test_expansion(self):
        test_observation = cosmic.Observation(test_data)
        result = test_observation.expansion()
        expected_result = ([3, 7], [2, 5, 8])
        self.assertEqual(result, expected_result)

    def test_path_lengths_large(self):
        test_observation = cosmic.Observation(test_data)
        result = test_observation.calculate_shortest_paths_large(2)
        expected_result = 374
        self.assertEqual(result, expected_result)

    def test_path_lengths_large_extended(self):
        test_observation = cosmic.Observation(test_data)
        result_1 = test_observation.calculate_shortest_paths_large(10)
        result_2 = test_observation.calculate_shortest_paths_large(100)
        expected_result_1 = 1030
        expected_result_2 = 8410
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))


if __name__ == "__main__":
    unittest.main()
