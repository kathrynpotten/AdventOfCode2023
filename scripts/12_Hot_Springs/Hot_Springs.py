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


def possible_configurations(spring_row, order):
    for i in range(len(spring_row)):
        index = i
        item = spring_row[i]
        if len(order) == 0:
            for i in range(index, len(spring_row)):
                if spring_row[i] == "?":
                    spring_row[i] = "."
            break
        elif item == "?":
            grouping = order[0]
            if (
                all(spring_row[index + x] == "?" for x in range(1, grouping))
                and not type(spring_row[index + grouping]) == int
            ):
                spring_row[index] = grouping
                if spring_row[index + grouping] == "?":
                    spring_row[index + grouping] = "."
                spring_row = spring_row[: index + 1] + spring_row[index + grouping :]
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
    previous_row = spring_row
    new_spring_row = spring_row
    for iteration in range(3):
        previous_row, new_spring_row, possible = test_arrangement(
            new_spring_row, previous_row, order, iteration
        )
        possibilities += possible

    return possibilities


def test_arrangement(spring_row, previous_row, order, iteration):
    original_row = spring_row.copy()
    new_row, order_residual = possible_configurations(spring_row, order)
    if len(order_residual) == 0:
        new_row_copy = new_row
        set_indices = []
        possible = 1
        for spring_set in order:
            set_index = new_row_copy.index(spring_set)
            set_indices.append(set_index)
            new_row_copy = new_row_copy[1:]
        for set_index in set_indices:
            new_spring_row = original_row.copy()
            if original_row[set_index] == "?":
                new_spring_row[set_index] == "."
            new_row, order_residual = possible_configurations(spring_row, order)

    else:
        possible = 0
        new_spring_row = original_row.copy()
        for spring_set in order[iteration:]:
            set_index = previous_row.index(spring_set)
            if original_row[set_index] == "?":
                new_spring_row[set_index] == "."
                break

    return new_row, new_spring_row, possible
