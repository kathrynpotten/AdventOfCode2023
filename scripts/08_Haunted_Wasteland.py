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

test_result = 2
test_result_2 = 6


def parse_map(input_data):
    instructions = input_data[0]
    node_list = input_data[1].split("\n")
    nodes = {node.split(" = ")[0]: node.split(" = ")[1] for node in node_list}
    for node, pos in nodes.items():
        pos_left = pos.split(", ")[0].replace("(", "")
        pos_right = pos.split(", ")[1].replace(")", "")
        nodes[node] = (pos_left, pos_right)
    return instructions, nodes


assert parse_map(test_data_2) == (
    "LLR",
    {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ"),
    },
)


def walk(instructions, nodes):
    current_node = "AAA"
    goal = "ZZZ"
    steps = 0

    def instruction_loop(current_node, goal, steps):
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                current_node = nodes[current_node][0]
            elif instruction == "R":
                current_node = nodes[current_node][1]
            if current_node == goal:
                break
        return current_node, steps

    while current_node != goal:
        current_node, steps = instruction_loop(current_node, goal, steps)

    return steps


test_instr, test_nodes = parse_map(test_data)
assert walk(test_instr, test_nodes) == test_result

test_instr_2, test_nodes_2 = parse_map(test_data_2)
assert walk(test_instr_2, test_nodes_2) == test_result_2


with open("../input_data/08_Haunted_Wasteland.txt", "r", encoding="utf-8") as file:
    input_data = file.read().strip().split("\n\n")

answer_instr, answer_nodes = parse_map(input_data)
answer_1 = walk(answer_instr, answer_nodes)
print(answer_1)
