import unittest
import Mirage_Maintenance_Testing as mirage


class Test(unittest.TestCase):
    def test_seq_of_differences(self):
        value = [0, 3, 6, 9, 12, 15]
        history = mirage.History(value)
        result = history.sequence_of_differences()
        expected_result = [3, 3, 3, 3, 3]
        self.assertEqual(result, expected_result)

    def test_difference_iter(self):
        value = [0, 3, 6, 9, 12, 15]
        history = mirage.History(value)
        result = history.differences_iter()
        expected_result = [value, [3, 3, 3, 3, 3], [0, 0, 0, 0]]
        self.assertEqual(result, expected_result)

    def test_next_value(self):
        value = [0, 3, 6, 9, 12, 15]
        history = mirage.History(value)
        history.differences_iter()
        result = history.next_value()
        self.assertEqual(result, 18)

    def test_previous_value(self):
        value = [10, 13, 16, 21, 30, 45]
        history = mirage.History(value)
        history.differences_iter()
        result = history.previous_value()
        self.assertEqual(result, 5)

    def test_sum_next(self):
        test_data = (
            """0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45""".strip().split("\n")
        )
        test_result = 114
        self.assertEqual(mirage.sum_of_extrapolated(test_data), test_result)

    def test_sum_previous(self):
        test_data = (
            """0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45""".strip().split("\n")
        )
        test_result = 2
        self.assertEqual(mirage.sum_of_extrapolated(test_data, "previous"), test_result)


if __name__ == "__main__":
    unittest.main()
