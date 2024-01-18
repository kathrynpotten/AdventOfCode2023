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


def check_possible_spring_placement(total_springs, row, index, grouping):
    for new_index, next_item in enumerate(row[index + 1 :]):
        if next_item == ".":
            for x in range(new_index):
                if type(row[index + x]) == str:
                    row[index + x] = "."
            break
        elif type(next_item) == int:
            if next_item + total_springs == grouping:
                row[index] = grouping
                if row[index + grouping] == "?":
                    row[index + grouping] = "."
                row = row[: index + 1] + row[index + new_index :]
                order = order[1:]
            elif next_item + total_springs > grouping:
                for x in range(new_index + 1):
                    if type(row[index + x]) == str:
                        row[index + x] = "."
                break
            elif next_item + total_springs < grouping:
                total_springs += next_item + new_index
        elif next_item == "?":
            total_springs += 1
    return row


def possible_configurations(input_row, order):
    spring_row = input_row.copy()
    for i in range(len(spring_row)):
        if i == len(spring_row):
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
                if all(spring_row[index + x] == "?" for x in range(grouping)):
                    if index + grouping >= len(spring_row):
                        break
                    elif not type(spring_row[index + grouping]) == int:
                        spring_row[index] = grouping
                        if spring_row[index + grouping] == "?":
                            spring_row[index + grouping] = "."
                        spring_row = (
                            spring_row[: index + 1] + spring_row[index + grouping :]
                        )
                        order = order[1:]
                else:
                    total_springs = 1
                    spring_row = check_possible_spring_placement(
                        total_springs, spring_row, index, grouping
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
                    if spring_row[index + 1] == ".":
                        break
                    elif spring_row[index + 1] == "?":
                        total_springs = item
                        spring_row = check_possible_spring_placement(
                            total_springs, spring_row, index, grouping
                        )

    return spring_row, order


def count_possible_configurations(spring_row, order):
    possibilities = 0
    possibilities += test_possible_configurations(spring_row, order, possibilities)

    return possibilities


def test_arrangement(input_row, order):
    output_arrangement, order_residual = possible_configurations(input_row, order)
    print(f"output is {output_arrangement}")
    if not order_residual:
        set_indices_dict = {}
        for spring_set in order:
            if spring_set in set_indices_dict:
                past_index = set_indices_dict[spring_set][0]
                set_indices_dict[spring_set] = [
                    past_index,
                    output_arrangement[past_index + 1 :].index(spring_set)
                    + past_index
                    + 1,
                ]
            else:
                set_indices_dict[spring_set] = [output_arrangement.index(spring_set)]
        set_indices = sum(set_indices_dict.values(), [])
        return set_indices
    else:
        return False


def test_possible_configurations(spring_row, order, possibilities):
    set_indices = test_arrangement(spring_row, order)
    if set_indices:
        possibilities += 1
        for set_index in set_indices:
            input_row = spring_row.copy()
            if spring_row[set_index] == "?":
                input_row[set_index] = "."
                possibilities = test_possible_configurations(
                    input_row, order, possibilities
                )

    return possibilities
