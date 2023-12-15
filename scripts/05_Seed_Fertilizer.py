import math

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


def map_converter_range(map, source):
    destinations = []
    remaining = source
    for line in map:
        map_start = int(line.split(" ")[1])
        map_length = int(line.split(" ")[2])
        map_end = map_start + map_length - 1
        offset = int(line.split(" ")[0]) - map_start
        # start of seed range maps
        if map_start <= source[0] <= map_end:
            # full overlap
            if source[0] + source[1] - 1 <= map_end:
                destinations.append((source[0] + offset, source[1]))
            # partial overlap
            else:
                len_overlap = map_end - source[0] + 1
                destinations.append((source[0] + offset, len_overlap))
                remaining = (map_end + 1, source[0] + source[1] - map_end)
        # end of seed range maps but start does not
        elif map_start <= source[0] + source[1] - 1 <= map_end:
            len_overlap = source[0] + source[1] - map_start
            destinations.append((map_start + offset, len_overlap))
            remaining = (source[0], map_start - source[0])
        # part of seed range maps but neither start nor end does
        elif source[0] < map_start and source[0] + source[1] > map_end:
            destinations.append((map_start + offset, map_length))
            remaining = [
                (source[0], map_start - source[0]),
                (map_end + 1, source[0] + source[1] - map_end),
            ]
    if sum([num_range[1] for num_range in destinations]) != source[1]:
        destinations.append(remaining)
    return destinations


assert map_converter_range(soil_map, (79, 14)) == [(81, 14)]
assert map_converter_range(soil_map, (45, 11)) == [(52, 6), (45, 5)]


def seed_ranges(seeds):
    input_list = seeds.split("seeds: ")[-1]
    seed_list = [int(seed) for seed in input_list.split(" ")]
    return [(seed_list[i], seed_list[i + 1]) for i in range(0, len(seed_list), 2)]


assert seed_ranges(test_data[0]) == [(79, 14), (55, 13)]


def find_location_numbers_range(seeds, maps):
    locations = []
    remains = {}
    for seed_range in seeds:
        source = seed_range
        for num, map in enumerate(maps):
            source = map_converter_range(map, source)
            if len(source) == 1:
                source = source[0]
            else:
                old_source = source
                source = old_source[0]
                remains[old_source[1]] = num
        locations.append(source[0])
    while remains:
        new_remains = remains.copy()
        for seed_range, map_num in remains.items():
            del new_remains[seed_range]
            remaining_loc, add_remains = find_location_numbers_range(
                [seed_range], maps[map_num + 1 :]
            )
            locations.extend(remaining_loc)
            new_remains.update(add_remains)
        remains = new_remains
    return locations, remains


def lowest_location_of_seed_ranges(input):
    maps = parse_data(input)
    seeds = seed_ranges(input[0])
    locations = find_location_numbers_range(seeds, maps)[0]
    return lowest_location(locations)


assert lowest_location_of_seed_ranges(test_data) == test_result_2

answer_2 = lowest_location_of_seed_ranges(input)
print(answer_2)
