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

test_result = 4


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


if __name__ == "__main__":
    unittest.main()
