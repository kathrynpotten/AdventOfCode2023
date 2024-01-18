import unittest
import Hot_Springs as springs


class Test(unittest.TestCase):
    def test_parse_line(self):
        test_string = "???.### 1,1,3"
        result = springs.parse_line(test_string)
        expected_result = "???.###", [1, 1, 3]
        self.assertEqual(result, expected_result)

    def test_replace_springs(self):
        test_string_1 = "???.### 1,1,3"
        spring_string_1 = springs.parse_line(test_string_1)[0]
        result_1 = springs.replace_springs(spring_string_1)
        expected_result_1 = ["?", "?", "?", ".", 3]
        test_string_2 = "?###???????? 3,2,1"
        spring_string_2 = springs.parse_line(test_string_2)[0]
        result_2 = springs.replace_springs(spring_string_2)
        expected_result_2 = ["?", 3, "?", "?", "?", "?", "?", "?", "?", "?"]
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))

    """def test_replace_springs_2(self):
        test_string_1 = "?###?...???? 3,2,1"
        spring_string_1 = springs.parse_line(test_string_1)[0]
        result_1 = springs.replace_springs(spring_string_1)
        expected_result_1 = ["?", 3, "?", ".", ".", ".", "?", "?", "?", "?"]
        self.assertEqual((result_1), (expected_result_1))"""

    """def test_possible_configurations(self):
        test_string_1 = "???.### 1,1,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1)[0]
        expected_result_1 = [1, ".", 1, ".", 3]
        test_string_2 = "?###???????? 3,2,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2)[0]
        expected_result_2 = [".", 3, ".", 2, ".", 1, ".", ".", "."]
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))"""

    def test_count_possibilities(self):
        test_string_1 = "???.### 1,1,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.count_possible_configurations(spring_row_1, order_1)
        expected_result_1 = 1
        print("\n")
        print("Test 2")
        test_string_2 = "?###???????? 3,2,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.count_possible_configurations(spring_row_2, order_2)
        expected_result_2 = 10
        self.assertEqual((result_1, result_2), (expected_result_1, expected_result_2))


if __name__ == "__main__":
    unittest.main()
