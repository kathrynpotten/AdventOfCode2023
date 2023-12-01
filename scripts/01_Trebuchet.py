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
