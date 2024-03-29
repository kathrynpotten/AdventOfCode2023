import math


def parse_line(input_data):
    spring_string = input_data.split(" ")[0]
    order = input_data.split(" ")[1].split(",")
    order = [int(num) for num in order]
    return spring_string, order


def replace_springs(spring_string):
    spring_row = [item for item in spring_string]
    count = 0
    for i in range(len(spring_string)):
        if spring_row[i] == "#" and i == len(spring_string) - 1:
            count += 1
            spring_row[i] = count
        elif spring_row[i] == "#":
            count += 1
        else:
            if i > 0 and spring_row[i - 1] == "#":
                spring_row[i - 1] = count
            count = 0

    spring_row = [item for item in spring_row if item != "#"]
    return spring_row


def check_possible_spring_placement(
    total_springs, row, index, grouping, order, set_indices_dict, index_tally
):
    index_count = index
    for new_index, next_item in enumerate(row[index + 1 :]):
        index_count += 1

        if total_springs == grouping:
            if type(row[index_count]) == int:
                if type(row[index]) == str:
                    row[index] = "."
                break
            elif sum(order[1:]) <= sum(
                [item for item in row[index_count:] if type(item) == int]
            ) and order[1:] != [
                item for item in row[index_count:] if type(item) == int
            ]:
                break
            else:
                row[index] = grouping
                if index_count < len(row) and row[index_count] == "?":
                    row[index_count] = "."
                row = row[: index + 1] + row[index_count:]
                order = order[1:]
                set_indices_dict[grouping].append(index + index_tally)
                index_tally += index_count - index - 1
                break

        elif next_item == ".":
            if type(row[index]) == str:
                row[index] = "."
            for x in range(new_index):
                if type(row[index + x]) == str:
                    row[index + x] = "."
            break
        elif type(next_item) == int:
            if next_item + total_springs == grouping:
                if sum(order[1:]) <= sum(
                    [item for item in row[index_count + 1 :] if type(item) == int]
                ) and order[1:] != [
                    item for item in row[index_count + 1 :] if type(item) == int
                ]:
                    break
                else:
                    row[index] = grouping
                    if index_count + 1 < len(row) and row[index_count + 1] == "?":
                        row[index_count + 1] = "."
                    row = row[: index + 1] + row[index_count + 1 :]
                    order = order[1:]
                    set_indices_dict[grouping].append(index + index_tally)
                    index_tally += index_count - index
                    break
            elif next_item + total_springs > grouping:
                row[index] = "."
                break
            elif next_item + total_springs < grouping:
                total_springs += next_item
        elif next_item == "?":
            total_springs += 1
            if new_index == len(row[index + 1 :]) - 1:
                if total_springs == grouping:
                    row[index] = grouping
                    row = row[: index + 1]
                    order = order[1:]

                    set_indices_dict[grouping].append(index + index_tally)

    return row, order, index_tally, set_indices_dict


def possible_configurations(input_row, order, original_row):
    possible = False
    spring_row = input_row.copy()
    original_order = order.copy()
    force_break = False
    set_indices_dict = {spring_set: [] for spring_set in order}
    index_tally = 0
    final_indices = []

    for i in range(len(spring_row)):
        remaining_springs = sum([i for i in spring_row[i:] if type(i) == int])
        possible_spaces = spring_row[i:].count("?")
        current_springs = [i for i in spring_row[:i] if type(i) == int]
        for j in range(len(current_springs)):
            if current_springs[j] != original_order[j]:
                force_break = True
                break
        if force_break:
            break

        spring_sets = [item for item in spring_row if type(item) == int]
        if spring_sets == original_order:
            spring_row = [item if item != "?" else "." for item in spring_row]
            order = []
            break

        if i == len(spring_row):
            break
        elif sum(order) > possible_spaces + remaining_springs:
            break
        else:
            index = i
            item = spring_row[i]

            if len(order) == 0:
                for i in range(index, len(spring_row)):
                    if spring_row[i] == "?":
                        spring_row[i] = "."
                break
            elif item == "?":
                grouping = order[0]
                if index + grouping > len(spring_row) and all(
                    type(item) == str for item in spring_row[index:]
                ):
                    break
                if all(spring_row[index + x] == "?" for x in range(grouping)):
                    if index + grouping == len(spring_row):
                        spring_row[index] = grouping
                        spring_row = (
                            spring_row[: index + 1] + spring_row[index + grouping :]
                        )
                        order = order[1:]
                        set_indices_dict[grouping].append(index + index_tally)
                        index_tally += grouping - 1
                    elif type(spring_row[index + grouping]) != int:
                        if sum(order[1:]) <= sum(
                            [
                                item
                                for item in spring_row[index + grouping :]
                                if type(item) == int
                            ]
                        ) and order[1:] != [
                            item
                            for item in spring_row[index + grouping :]
                            if type(item) == int
                        ]:
                            continue
                        spring_row[index] = grouping
                        if spring_row[index + grouping] == "?":
                            spring_row[index + grouping] = "."
                        spring_row = (
                            spring_row[: index + 1] + spring_row[index + grouping :]
                        )
                        order = order[1:]
                        set_indices_dict[grouping].append(index + index_tally)

                        index_tally += grouping - 1
                    else:
                        spring_row[index] = "."

                else:
                    total_springs = 1
                    (
                        spring_row,
                        order,
                        index_tally,
                        set_indices_dict,
                    ) = check_possible_spring_placement(
                        total_springs,
                        spring_row,
                        index,
                        grouping,
                        order,
                        set_indices_dict,
                        index_tally,
                    )
            elif type(item) == int:
                grouping = order[0]
                if item == grouping:
                    if index + 1 < len(spring_row) and spring_row[index + 1] == "?":
                        spring_row[index + 1] = "."
                    order = order[1:]
                elif item > grouping:
                    if index + 1 < len(spring_row) and spring_row[index + 1] == "?":
                        spring_row[index + 1] = "."
                elif item < grouping:
                    if index + 1 >= len(spring_row):
                        break
                    elif spring_row[index + 1] == ".":
                        continue
                    elif spring_row[index + 1] == "?":
                        total_springs = item
                        (
                            spring_row,
                            order,
                            index_tally,
                            set_indices_dict,
                        ) = check_possible_spring_placement(
                            total_springs,
                            spring_row,
                            index,
                            grouping,
                            order,
                            set_indices_dict,
                            index_tally,
                        )

    spring_sets = [item for item in spring_row if type(item) == int]
    if spring_sets == original_order:
        possible = True
        order = []
        return (spring_row, order, possible, set_indices_dict, final_indices)
    elif (
        spring_sets != original_order
        and (len(spring_sets) > len(original_order) or force_break)
        and spring_sets
    ):
        seen_indices = []
        for spring_set in spring_sets:
            new_input_row = input_row.copy()
            initial_index = spring_row.index(spring_set)

            if initial_index in seen_indices:
                temp_index = spring_row[initial_index + 1 :].index(spring_set)
                initial_index = initial_index + 1 + temp_index
            seen_indices.append(initial_index)

            current_space_count = initial_index + sum(
                [item - 1 for item in spring_row[:initial_index] if type(item) == int]
            )
            input_space_count = 0
            for index, item in enumerate(original_row):
                if input_space_count == current_space_count:
                    final_index = index
                if type(item) == int:
                    input_space_count += item
                else:
                    input_space_count += 1
            if type(original_row[final_index]) != int:
                new_input_row[final_index] = "."
                final_indices.append(final_index)
                (
                    output_row,
                    order,
                    possible,
                    set_indices_dict,
                    output_indices,
                ) = possible_configurations(new_input_row, original_order, original_row)
                if possible:
                    spring_row = output_row
                    break
            else:
                continue

    return spring_row, order, possible, set_indices_dict, final_indices


def test_arrangement(input_row, order, original_row):
    (
        output_arrangement,
        order_residual,
        possible,
        set_indices_dict,
        final_indices,
    ) = possible_configurations(input_row, order, original_row)

    if not order_residual:
        set_indices = sum(set_indices_dict.values(), [])
        set_indices.sort()
        return set_indices, final_indices
    else:
        return False, False


def loop_over_set_indices(
    spring_row, set_index, original_row, order, possibilities, seen
):
    input_row = spring_row.copy()
    original_space_count = set_index + sum(
        [item - 1 for item in original_row[:set_index] if type(item) == int]
    )
    input_space_count = 0
    final_index = set_index
    for index, item in enumerate(input_row):
        if input_space_count == original_space_count:
            final_index = index
            break
        elif type(item) == int:
            input_space_count += item
        else:
            input_space_count += 1
    remaining_length = len(spring_row) - final_index
    if spring_row[final_index] == "?":
        for x in range(remaining_length):
            if spring_row[final_index + x] == "?":
                input_row[final_index + x] = "."
                # print(spring_row, input_row, final_index, final_index + x)
                possibilities, seen = test_possible_configurations(
                    input_row, order, possibilities, seen, original_row
                )
            else:
                break
        for x in range(1, remaining_length):
            input_row = spring_row.copy()
            if spring_row[final_index + x] == "?":
                input_row[final_index + x] = "."
                # print(spring_row, input_row, final_index, final_index + x)
                possibilities, seen = test_possible_configurations(
                    input_row, order, possibilities, seen, original_row
                )
            else:
                break
    return possibilities, seen


def test_possible_configurations(spring_row, order, possibilities, seen, original_row):
    total_springs = sum([i for i in spring_row if type(i) == int])
    possible_spaces = spring_row.count("?")
    if total_springs + possible_spaces < sum(order):
        return possibilities, seen
    elif (
        total_springs == sum(order)
        and [i for i in spring_row if type(i) == int] == order
    ):
        possibilities += 1
        return possibilities, seen

    set_indices, final_indices = test_arrangement(spring_row, order, original_row)

    if set_indices != False and set_indices not in seen:
        seen.append(set_indices)
        possibilities += 1

        for i in final_indices:
            remaining_length = len(spring_row) - i

            for x in range(remaining_length):
                temp_row = spring_row.copy()
                if spring_row[i + x] == "?":
                    temp_row[i + x] = "."

                    for set_index in set_indices:
                        possibilities, seen = loop_over_set_indices(
                            temp_row,
                            set_index,
                            original_row,
                            order,
                            possibilities,
                            seen,
                        )
                elif spring_row[i + x] == ".":
                    break

        for set_index in set_indices:
            possibilities, seen = loop_over_set_indices(
                spring_row,
                set_index,
                original_row,
                order,
                possibilities,
                seen,
            )
    return possibilities, seen


def count_possible_configurations(spring_row, order):
    possibilities = 0
    seen = []
    original_row = spring_row.copy()
    possibilities = test_possible_configurations(
        spring_row, order, possibilities, seen, original_row
    )[0]
    return possibilities


def sum_of_arrangements(input_strings):
    sum = 0
    for num, springs in enumerate(input_strings):
        spring_string, order = parse_line(springs)
        spring_row = replace_springs(spring_string)
        print(f"{num}:{spring_string} {spring_row}, {order}")
        possible = count_possible_configurations(spring_row, order)
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


def unfolded(input_strings):
    sum = 0
    for num, springs in enumerate(input_strings):
        spring_string, order = parse_line(springs)
        spring_row = replace_springs(spring_string)
        print(f"{num}:{spring_string} {spring_row}, {order}")
        possible_original = count_possible_configurations(spring_row, order)
        spring_row.append("?")
        possible_extended = count_possible_configurations(spring_row, order)
        possible = (possible_extended**4) * possible_original
        print(possible)
        sum += possible
    return sum


if __name__ == "__main__":
    with open("../../input_data/12_Hot_Springs.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip().split("\n")

    answer_1 = sum_of_arrangements(input_data)
    print(answer_1)

    # 618 incorrect - one fewer than expected. Also gained two extra from somewhere ...  - 308 and 469
    # correct : 7753
