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
