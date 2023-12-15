test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".strip().split(
    "\n\n"
)

test_data_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".strip().split(
    "\n\n"
)


def parse_map(input_data):
    instructions = input_data[0]
    node_list = input_data[1].split("\n")
    nodes = {node.split(" = ")[0]: node.split(" = ")[1] for node in node_list}
    return instructions, nodes


print(parse_map(test_data_2))
assert parse_map(test_data_2) == (
    "LLR",
    {
        "AAA": "(BBB, BBB)",
        "BBB": "(AAA, ZZZ)",
        "ZZZ": "(ZZZ, ZZZ)",
    },
)
