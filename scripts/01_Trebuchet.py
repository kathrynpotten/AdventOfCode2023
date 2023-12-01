test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".strip().split(
    "\n"
)

test_result = 142


def calibration_values(input):
    sum = 0
    for line in input:
        for element in line:
            if element.isdigit():
                calibration = element
                break
        for element in line[::-1]:
            if element.isdigit():
                calibration += element
                break
        sum += int(calibration)
    return sum


assert calibration_values(test_data) == test_result

with open("../input_data/01_Trebuchet.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n")

answer_1 = calibration_values(input)
print(answer_1)


""" Part Two """


test_data_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".strip().split(
    "\n"
)

test_result_2 = 281

digit_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def updated_calibration_values(input):
    sum = 0
    for line in input:
        indices = {}
        if any(digit in line for digit in digit_dict):
            for digit in digit_dict:
                check_line = line
                while digit in check_line:
                    indices[check_line.index(digit)] = digit_dict[digit]
                    check_line = check_line.replace(digit, "z" * len(digit), 1)
            for index, element in enumerate(line):
                if element.isdigit():
                    indices[index] = element
        else:
            for index, element in enumerate(line):
                if element.isdigit():
                    indices[index] = element
        sorted_indices = sorted(indices)
        calibration = str(indices[sorted_indices[0]]) + str(indices[sorted_indices[-1]])
        sum += int(calibration)
    return sum


test_line = ["eightwothree"]
# assert updated_calibration_values(test_line) == 83
# assert updated_calibration_values(test_data_2) == test_result_2

test_line_2 = ["sevenlnmnzh35fivetwotrbnknfive"]
# print(updated_calibration_values(test_line_2))

answer_2 = updated_calibration_values(input)
print(answer_2)
