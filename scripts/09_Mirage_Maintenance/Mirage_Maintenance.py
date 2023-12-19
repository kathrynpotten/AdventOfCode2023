class History:
    def __init__(self, value):
        self.value = value
        self.differences = [value]

    def sequence_of_differences(self):
        difference = self.differences[-1]
        differences = [
            difference[i + 1] - difference[i] for i in range(len(difference) - 1)
        ]
        self.differences.append(differences)
        return differences

    def differences_iter(self):
        difference = self.differences[0]
        while len(set(difference)) != 1:
            difference = self.sequence_of_differences()
        self.differences.append([0] * (len(difference) - 1))
        return self.differences

    def next_value(self):
        self.differences = self.differences[::-1]
        new_value = self.differences[1][-1]
        for i in range(2, len(self.differences)):
            new_value += self.differences[i][-1]
        return new_value

    def previous_value(self):
        self.differences = self.differences[::-1]
        new_value = self.differences[1][0]
        for i in range(2, len(self.differences)):
            new_value = self.differences[i][0] - new_value
        return new_value


def sum_of_extrapolated(input_data, extrap_type="next"):
    sum = 0
    for line in input_data:
        values = line.split(" ")
        history = History([int(value) for value in values])
        history.differences_iter()
        if extrap_type == "next":
            sum += history.next_value()
        elif extrap_type == "previous":
            sum += history.previous_value()
    return sum


if __name__ == "__main__":
    with open(
        "../../input_data/09_Mirage_Maintenance.txt", "r", encoding="utf-8"
    ) as file:
        input_data = file.read().strip().split("\n")

    answer_1 = sum_of_extrapolated(input_data)
    print(answer_1)

    answer_2 = sum_of_extrapolated(input_data, "previous")
    print(answer_2)
