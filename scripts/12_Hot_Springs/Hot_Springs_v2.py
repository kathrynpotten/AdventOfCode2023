import itertools


def parse_line(input_data):
    spring_string = input_data.split(" ")[0] + "."
    order = input_data.split(" ")[1].split(",")
    order = [int(num) for num in order]
    return spring_string, order


def count_possible_configurations(spring_string, order):
    possibilities = 0
    positions = {0: 1}
    for i, grouping in enumerate(order):
        new_positions = {}
        for position, possibility in positions.items():
            for index in range(
                position,
                len(spring_string) - (sum(order[i + 1 :]) + len(order[i + 1 :])),
            ):
                if (index + grouping - 1) < len(
                    spring_string
                ) and "." not in spring_string[index : index + grouping]:
                    if (
                        i == len(order) - 1
                        and "#" not in spring_string[index + grouping :]
                    ) or (
                        i < len(order) - 1 and spring_string[index + grouping] != "#"
                    ):
                        if index + grouping + 1 in new_positions:
                            new_positions[index + grouping + 1] += possibility
                        else:
                            new_positions[index + grouping + 1] = possibility
                if spring_string[index] == "#":
                    break
        positions = new_positions
    possibilities = sum(positions.values())
    return possibilities


def sum_of_arrangements(input_strings):
    sum = 0
    for num, springs in enumerate(input_strings):
        spring_string, order = parse_line(springs)
        print(f"{num}:{spring_string} {order}")
        possible = count_possible_configurations(spring_string, order)
        print(possible)

        sum += possible
    return sum


def update_input_strings(input_springs):
    updated_input = []
    for spring in input_springs:
        spring_string = spring.split(" ")[0]
        order = spring.split(" ")[1]
        new_spring_string = ((spring_string + "?") * 4) + spring_string
        new_order = (order + ",") * 4 + order
        updated_input.append(new_spring_string + " " + new_order)
    return updated_input


if __name__ == "__main__":
    with open("../../input_data/12_Hot_Springs.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip().split("\n")

    answer_1 = sum_of_arrangements(input_data)
    print(answer_1)

    updated_input_data = update_input_strings(input_data)
    answer_2 = sum_of_arrangements(updated_input_data)
    print(answer_2)
