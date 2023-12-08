import re

test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().split(
    "\n"
)

test_result = 13


def parse_card(card):
    winning = card.split(" | ")[0].split(": ")[1]
    winning_numbers = re.findall(r"\d+", winning)
    mine = card.split(" | ")[1]
    my_numbers = re.findall(r"\d+", mine)
    return list(map(int, winning_numbers)), list(map(int, my_numbers))


test_card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
assert parse_card(test_card) == ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])


def find_winning_numbers(winning_numbers, my_numbers):
    matching_numbers = [num for num in my_numbers if num in winning_numbers]
    return len(matching_numbers)


def calculate_points(num_matching, num_winning):
    points_dict = {x: 2 ** (x - 1) for x in range(1, num_winning + 1)}
    points_dict[0] = 0
    return points_dict[num_matching]


def scratchcards_total(cards):
    points = 0
    for card in cards:
        winning_numbers, my_numbers = parse_card(card)
        num_matching = find_winning_numbers(winning_numbers, my_numbers)
        points += calculate_points(num_matching, len(winning_numbers))
    return points


assert scratchcards_total(test_data) == test_result


with open("../input_data/04_Scratchcards.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n")

answer_1 = scratchcards_total(input)
print(answer_1)
