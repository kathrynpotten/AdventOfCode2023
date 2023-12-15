test_data = """Time:      7  15   30
Distance:  9  40  200
""".strip().split(
    "\n"
)

test_result = 288
test_result_2 = 71503


def range_of_distances(time):
    return [(time - x) * x for x in range(time + 1)]


assert range_of_distances(7) == [0, 6, 10, 12, 12, 10, 6, 0]


def num_winning_distances(range, record):
    return sum([dist > record for dist in range])


test_range = [0, 6, 10, 12, 12, 10, 6, 0]
assert num_winning_distances(test_range, 9) == 4

test_range_2 = [
    0,
    29,
    56,
    81,
    104,
    125,
    144,
    161,
    176,
    189,
    200,
    209,
    216,
    221,
    224,
    225,
    224,
    221,
    216,
    209,
    200,
    189,
    176,
    161,
    144,
    125,
    104,
    81,
    56,
    29,
    0,
]
assert num_winning_distances(test_range_2, 200) == 9


def num_ways_to_beat(race_list):
    product = 1
    times = race_list[0].split()[1:]
    records = race_list[1].split()[1:]
    for time, record in zip(times, records):
        time_range = [(int(time) - x) * x for x in range(int(int(time) / 2) + 1)]
        if (int(time) + 1) % 2 == 0:
            product *= num_winning_distances(time_range, int(record)) * 2
        else:
            product *= num_winning_distances(time_range, int(record)) * 2 - 1
    return product


assert num_ways_to_beat(test_data) == test_result


def num_ways_to_beat_single(race):
    time = "".join(race[0].split()[1:])
    record = "".join(race[1].split()[1:])
    time_range = [(int(time) - x) * x for x in range(int(int(time) / 2) + 1)]
    if (int(time) + 1) % 2 == 0:
        return num_winning_distances(time_range, int(record)) * 2
    else:
        return num_winning_distances(time_range, int(record)) * 2 - 1


assert num_ways_to_beat_single(test_data) == test_result_2


with open("../input_data/06_Wait_For_It.txt", "r", encoding="utf-8") as file:
    input_data = file.read().strip().split("\n")


answer_1 = num_ways_to_beat(input_data)
print(answer_1)


answer_2 = num_ways_to_beat_single(input_data)
print(answer_2)
