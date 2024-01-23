import unittest
import Hot_Springs as springs

test_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".strip().split(
    "\n"
)


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

    def test_replace_springs_2(self):
        test_string_1 = "?###?...???? 3,2,1"
        spring_string_1 = springs.parse_line(test_string_1)[0]
        result_1 = springs.replace_springs(spring_string_1)
        expected_result_1 = ["?", 3, "?", ".", ".", ".", "?", "?", "?", "?"]
        self.assertEqual((result_1), (expected_result_1))

    def test_possible_configurations(self):
        test_string_1 = "???.### 1,1,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [1, ".", 1, ".", 3]

        test_string_2 = "?###???????? 3,2,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [".", 3, ".", 2, ".", 1, ".", ".", "."]

        spring_row_3, order_3 = ["?", 3, "?", ".", ".", ".", "?", "?", "?", "?"], [
            3,
            2,
            1,
        ]
        result_3 = springs.possible_configurations(spring_row_3, order_3, spring_row_3)[
            0
        ]
        expected_result_3 = [".", 3, ".", ".", ".", ".", 2, ".", 1]
        self.assertEqual(
            (result_1, result_2, result_3),
            (expected_result_1, expected_result_2, expected_result_3),
        )

    def test_possible_configurations_2(self):
        test_string_1 = ".??..??...?##. 1,1,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [".", 1, ".", ".", ".", 1, ".", ".", ".", ".", 3, "."]

        test_string_2 = "????##?#??. 6,1,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [6, ".", 1, ".", 1, "."]

        test_string_3 = "##?#??#.?# 7,1"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.possible_configurations(spring_row_3, order_3, spring_row_3)[
            0
        ]
        expected_result_3 = [7, ".", ".", 1]
        self.assertEqual(
            (result_1, result_2, result_3),
            (expected_result_1, expected_result_2, expected_result_3),
        )

    def test_possible_configurations_2(self):
        test_string_1 = "?#?#?#?#?#?#?#? 1,3,1,6"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [".", 1, ".", 3, ".", 1, ".", 6]

        test_string_2 = "?##?##???? 7,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [7, ".", 1, "."]

        test_string_3 = "?#??#.????..?##? 1,2,3,4"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.possible_configurations(spring_row_3, order_3, spring_row_3)[
            0
        ]
        expected_result_3 = [".", 1, ".", 2, ".", 3, ".", ".", ".", 4]

        self.assertEqual(
            (result_1, result_2, result_3),
            (expected_result_1, expected_result_2, expected_result_3),
        )

    def test_possible_configurations_3(self):
        test_string_1 = "???????##?.??? 7,2"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [".", ".", 7, ".", ".", 2, "."]

        test_string_2 = "?..?????#####??.??? 1,2,7,3"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [1, ".", ".", 2, ".", 7, ".", ".", ".", 3]

        test_string_3 = "??????#.#?#?#?? 5,5"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.possible_configurations(spring_row_3, order_3, spring_row_3)[
            0
        ]
        expected_result_3 = [".", ".", 5, ".", 5, ".", "."]

        self.assertEqual(
            (result_1, result_2, result_3),
            (expected_result_1, expected_result_2, expected_result_3),
        )

    def test_possible_configurations_4(self):
        test_string_1 = "?.??#?#?.??.#.? 5,1"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [".", ".", 5, ".", ".", ".", ".", ".", 1, ".", "."]

        test_string_2 = "###????..#???#?? 5,1,2"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [5, ".", ".", ".", ".", 1, ".", ".", 2, ".", "."]

        test_string_3 = "?.??#????##????#.#? 1,1,4,3,1"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.possible_configurations(spring_row_3, order_3, spring_row_3)[
            0
        ]
        expected_result_3 = [".", ".", 1, ".", 1, ".", ".", 4, ".", ".", 3, ".", 1, "."]

        self.assertEqual(
            (result_1, result_2, result_3),
            (expected_result_1, expected_result_2, expected_result_3),
        )

    def test_possible_configurations_5(self):
        test_string_1 = ".??#.???????#?.???.? 1,7,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.possible_configurations(spring_row_1, order_1, spring_row_1)[
            0
        ]
        expected_result_1 = [".", ".", ".", 1, ".", ".", 7, ".", ".", 3, ".", "."]

        test_string_2 = "??.#??.###? 1,3"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.possible_configurations(spring_row_2, order_2, spring_row_2)[
            0
        ]
        expected_result_2 = [".", ".", ".", 1, ".", ".", ".", 3, "."]

        self.assertEqual(
            (result_1, result_2),
            (expected_result_1, expected_result_2),
        )

    def test_impossible(self):
        test_row = ["?", 3, "?", ".", ".", ".", ".", ".", ".", "?"]
        order = [3, 2, 1]
        result = springs.possible_configurations(test_row, order, test_row)[0]
        expected_result = [".", 3, ".", ".", ".", ".", ".", ".", ".", "?"]
        self.assertEqual(result, expected_result)

    def test_count_possibilities(self):
        test_string_1 = "???.### 1,1,3"
        spring_string_1, order_1 = springs.parse_line(test_string_1)
        spring_row_1 = springs.replace_springs(spring_string_1)
        result_1 = springs.count_possible_configurations(spring_row_1, order_1)[0]
        expected_result_1 = 1

        test_string_2 = "?###???????? 3,2,1"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.count_possible_configurations(spring_row_2, order_2)[0]
        expected_result_2 = 10

        test_string_3 = ".??..??...?##. 1,1,3"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.count_possible_configurations(spring_row_3, order_3)[0]
        expected_result_3 = 4

        test_string_4 = "?.??#????##????#.#? 1,1,4,3,1"
        spring_string_4, order_4 = springs.parse_line(test_string_4)
        spring_row_4 = springs.replace_springs(spring_string_4)
        result_4 = springs.count_possible_configurations(spring_row_4, order_4)[0]
        expected_result_4 = 5

        self.assertEqual(
            (result_1, result_2, result_3, result_4),
            (
                expected_result_1,
                expected_result_2,
                expected_result_3,
                expected_result_4,
            ),
        )

    def test_change_to_input_bug(self):
        test_row, order = [
            "?",
            ".",
            "?",
            "?",
            1,
            "?",
            "?",
            ".",
            "?",
            2,
            "?",
            "?",
            "?",
            "?",
            1,
            ".",
            1,
            "?",
        ], [1, 1, 4, 3, 1]
        original_row = test_row
        result = springs.possible_configurations(test_row, order, original_row)[0]
        expected_result = [".", ".", 1, ".", 1, ".", ".", ".", 4, ".", 3, ".", 1, "."]

        self.assertEqual(result, expected_result)

    def test_count_possibilities_2(self):
        test_row, order = [
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            ".",
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            1,
            "?",
            "?",
            1,
            "?",
        ], [1, 1, 1, 2, 7]
        result = springs.count_possible_configurations(test_row, order)[0]
        expected_result = 12

        test_string_2 = "??.#??.###? 1,3"
        spring_string_2, order_2 = springs.parse_line(test_string_2)
        spring_row_2 = springs.replace_springs(spring_string_2)
        result_2 = springs.count_possible_configurations(spring_row_2, order_2)[0]
        expected_result_2 = 1

        test_string_3 = "????#?#????????#?## 1,2,2,9"
        spring_string_3, order_3 = springs.parse_line(test_string_3)
        spring_row_3 = springs.replace_springs(spring_string_3)
        result_3 = springs.count_possible_configurations(spring_row_3, order_3)[0]
        expected_result_3 = 2

        self.assertEqual(
            (result, result_2, result_3),
            (expected_result, expected_result_2, expected_result_3),
        )

    def test_following_integer_bug(self):
        test_row, order = [
            ".",
            1,
            ".",
            ".",
            1,
            "?",
            1,
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            "?",
            1,
            "?",
            2,
        ], [1, 2, 2, 9]
        result = springs.count_possible_configurations(test_row, order)[0]
        expected_result = 0

        self.assertEqual(result, expected_result)

    def test_sum_of_arrangements(self):
        result = springs.sum_of_arrangements(test_data)
        expected_result = 21
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
