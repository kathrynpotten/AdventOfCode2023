test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip().split(
    "\n\n"
)

test_result = 35

test_result_2 = 46


def parse_data(input):
    maps_list = [map.split("map:\n")[-1] for map in input]
    maps = [map.split("\n") for map in maps_list[1:]]
    return maps


assert parse_data(test_data) == [
    ["50 98 2", "52 50 48"],
    ["0 15 37", "37 52 2", "39 0 15"],
    ["49 53 8", "0 11 42", "42 0 7", "57 7 4"],
    ["88 18 7", "18 25 70"],
    ["45 77 23", "81 45 19", "68 64 13"],
    ["0 69 1", "1 0 69"],
    ["60 56 37", "56 93 4"],
]


def intial_seed_numbers(seeds):
    seed_list = seeds.split("seeds: ")[-1]
    return [int(seed) for seed in seed_list.split(" ")]


def map_converter(map, source):
    destination = False
    # is source in range?
    for line in map:
        source_start = int(line.split(" ")[1])
        source_length = int(line.split(" ")[2])
        source_end = source_start + source_length
        if source in range(source_start, source_end):
            source_pos = source - source_start
            destination = int(line.split(" ")[0]) + source_pos
    if not destination:
        destination = source
    return destination


soil_map = ["50 98 2", "52 50 48"]
assert map_converter(soil_map, 99) == 51
assert map_converter(soil_map, 53) == 55


def find_location_numbers(seeds, maps):
    locations = []
    for seed in seeds:
        source = seed
        for map in maps:
            source = map_converter(map, source)
        locations.append(source)
    return locations


def lowest_location(locations):
    return min(locations)


def lowest_location_of_seeds(input):
    maps = parse_data(input)
    seeds = intial_seed_numbers(input[0])
    locations = find_location_numbers(seeds, maps)
    return lowest_location(locations)


assert lowest_location_of_seeds(test_data) == test_result


with open("../input_data/05_Seed_Fertilizer.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n\n")

answer_1 = lowest_location_of_seeds(input)
print(answer_1)


""" Part 2 """


def intial_seed_numbers_updated(seeds):
    input_list = seeds.split("seeds: ")[-1]
    seed_list = [int(seed) for seed in input_list.split(" ")]
    seeds = []
    for i in range(0, int(len(seed_list) / 2) + 1, 2):
        seed_start = seed_list[i]
        seed_length = seed_list[i + 1]
        seed_end = seed_start + seed_length
        seeds.extend([seed for seed in range(seed_start, seed_end)])
    return seeds


assert intial_seed_numbers_updated(test_data[0]) == [
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
]


def seed_list(seeds):
    input_list = seeds.split("seeds: ")[-1]
    seed_list = [int(seed) for seed in input_list.split(" ")]
    return {
        seed_list[i]: seed_list[i] + seed_list[i + 1]
        for i in range(0, int(len(seed_list) / 2) + 1, 2)
    }


def find_lowest_location(seeds, maps):
    lowest_loc = 999999999999
    for seed_start, seed_end in seeds.items():
        for num, seed in enumerate(range(seed_start, seed_end)):
            if num % 1000000 == 0:
                print(f"Iteration {num}")
            source = seed
            for map in maps:
                source = map_converter(map, source)
            lowest_loc = min(source, lowest_loc)
    return lowest_loc


# maps = parse_data(input)
# seeds = seed_list(input[0])
# answer_2 = find_lowest_location(seeds, maps)
# print(answer_2)

# work backwards - what is lowest possible location number? doe sit correspond to a seed?


def min_location_possible(loc_map):
    min_destination = 999999999999
    for line in loc_map:
        line_min_destination = int(line.split(" ")[0])
        if line_min_destination < min_destination:
            source = int(line.split(" ")[1])
            min_destination = line_min_destination
    return source


def map_converter_reverse(map, destination):
    source = False
    for line in map:
        destination_start = int(line.split(" ")[0])
        destination_length = int(line.split(" ")[2])
        destination_end = destination_start + destination_length
        if destination in range(destination_start, destination_end):
            destination_pos = destination - destination_start
            source = int(line.split(" ")[1]) + destination_pos
        if not source:
            source = destination
    return source


def seed_for_lowest_loc(maps):
    source = min_location_possible(maps[-1])
    for map in maps[::-1][1:]:
        source = map_converter_reverse(map, source)
    return source


test_maps = parse_data(test_data)
print(seed_for_lowest_loc(test_maps))

# iterate over possible locations until find a corresponding seed
