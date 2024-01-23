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


def check_possible_spring_placement(total_springs, row, index, grouping, order):
    index_count = index
    for new_index, next_item in enumerate(row[index + 1 :]):
        if total_springs == grouping:
            row[index] = grouping
            if index_count + 1 < len(row) and row[index_count + 1] == "?":
                row[index_count + 1] = "."
            row = row[: index + 1] + row[index_count + 1 :]
            order = order[1:]
            break
        index_count += 1
        if next_item == ".":
            if type(row[index]) == str:
                row[index] = "."
            for x in range(new_index):
                if type(row[index + x]) == str:
                    row[index + x] = "."
            break
        elif type(next_item) == int:
            if next_item + total_springs == grouping:
                row[index] = grouping
                if index_count + 1 < len(row) and row[index_count + 1] == "?":
                    row[index_count + 1] = "."
                row = row[: index + 1] + row[index_count + 1 :]
                order = order[1:]
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

    return row, order


def possible_configurations(input_row, order, original_row):
    possible = False
    spring_row = input_row.copy()
    original_order = order.copy()
    for i in range(len(spring_row)):
        if i == len(spring_row):
            break
        else:
            index = i
            item = spring_row[i]

            spring_sets = [item for item in spring_row if type(item) == int]
            if spring_sets == original_order:
                spring_row = [item if item != "?" else "." for item in spring_row]
                order = []
                break

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
                    elif not type(spring_row[index + grouping]) == int:
                        spring_row[index] = grouping
                        if spring_row[index + grouping] == "?":
                            spring_row[index + grouping] = "."
                        spring_row = (
                            spring_row[: index + 1] + spring_row[index + grouping :]
                        )
                        order = order[1:]
                    else:
                        spring_row[index] = "."

                else:
                    total_springs = 1
                    spring_row, order = check_possible_spring_placement(
                        total_springs, spring_row, index, grouping, order
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
                        spring_row, order = check_possible_spring_placement(
                            total_springs, spring_row, index, grouping, order
                        )

    spring_sets = [item for item in spring_row if type(item) == int]
    if spring_sets == original_order:
        possible = True
        return (spring_row, order, possible)
    elif (
        spring_sets != original_order
        and len(spring_sets) > len(original_order)
        and spring_sets
    ):
        for spring_set in spring_sets:
            new_input_row = input_row.copy()
            initial_index = spring_row.index(spring_set)
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
            if (
                original_row[final_index] != spring_set
                and type(original_row[final_index]) != int
            ):
                new_input_row[final_index] = "."
                output_row, order, possible = possible_configurations(
                    new_input_row, original_order, original_row
                )
                if possible:
                    spring_row = output_row
                    break
    return spring_row, order, possible


def test_arrangement(input_row, order, original_row):
    output_arrangement, order_residual, possible = possible_configurations(
        input_row, order, original_row
    )
    if not order_residual:
        print("\n")
        print(input_row)
        print(output_arrangement)
        set_indices_dict = {}
        for spring_set in order:
            if spring_set in set_indices_dict:
                past_index = set_indices_dict[spring_set][0]
                current_index = (
                    output_arrangement[past_index + 1 :].index(spring_set)
                    + past_index
                    + 1
                )
                set_indices_dict[spring_set] = [
                    past_index,
                    current_index,
                ]
            else:
                current_index = output_arrangement.index(spring_set)
                set_indices_dict[spring_set] = [current_index]
        for spring_set in set_indices_dict.keys():
            set_index = set_indices_dict[spring_set]
            for index in set_index:
                if original_row[index] == spring_set:
                    set_indices_dict[spring_set] = [i for i in set_index if i != index]

        set_indices = sum(set_indices_dict.values(), [])
        return set_indices
    else:
        return False


def test_possible_configurations(spring_row, order, possibilities, seen, original_row):
    set_indices = test_arrangement(spring_row, order, original_row)
    if set_indices:
        if set_indices not in seen:
            print(set_indices)
            seen.append(set_indices)
            possibilities += 1
            for set_index in set_indices:
                input_row = spring_row.copy()
                remaining_length = len(spring_row) - set_index
                if spring_row[set_index] == "?":
                    input_row[set_index] = "."
                    for x in range(1, remaining_length):
                        for i in range(x):
                            if spring_row[set_index + i] == "?":
                                input_row[set_index + i] = "."
                            possibilities, seen = test_possible_configurations(
                                input_row, order, possibilities, seen, original_row
                            )

    return possibilities, seen


def count_possible_configurations(spring_row, order):
    possibilities = 0
    seen = []
    original_row = spring_row.copy()
    possibilities += test_possible_configurations(
        spring_row, order, possibilities, seen, original_row
    )[0]
    # print(possibilities)
    error = False
    if possibilities == 0:
        error = True
    return possibilities, error


def sum_of_arrangements(input_strings):
    sum = 0
    errored = []
    for num, springs in enumerate(input_strings):
        spring_string, order = parse_line(springs)
        spring_row = replace_springs(spring_string)
        # if num == 19:
        #    print(f"{num}: {spring_string}, {spring_row}, {order}")

        print("\n")
        print(f"{num}: {spring_string}, {spring_row}, {order}")
        possible, error = count_possible_configurations(spring_row, order)
        sum += possible
        if error:
            errored.append(num)
    print(errored)
    return sum


if __name__ == "__main__":
    with open("../../input_data/12_Hot_Springs.txt", "r", encoding="utf-8") as file:
        input_data = file.read().strip().split("\n")

    input_data = input_data[:163] + input_data[164:]

    answer_1 = sum_of_arrangements(input_data)
    print(answer_1)

# too low 4429

# stuck on #163, error #792
