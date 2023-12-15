from collections import Counter

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".strip().split(
    "\n"
)

test_result = 5905

ranks = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
values = {rank: x for rank, x in zip(ranks, range(13))}
types = [
    "Five of A Kind",
    "Four of A Kind",
    "Full House",
    "Three of A Kind",
    "Two Pair",
    "One Pair",
    "High Card",
]
type_values = {hand_type: 6 - x for hand_type, x in zip(types, range(7))}


class Card:
    def __init__(self, rank):
        self.rank = rank
        self._value = values[rank]

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self.rank}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self) -> int:
        return hash(self.value)


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = None
        self.hand_value = None
        self.hand_type()

    def __str__(self):
        return f"{self.type}: {''.join([str(card) for card in self.cards])}"

    def hand_type(self):
        card_count = Counter(self.cards)
        if card_count.most_common()[0][1] == 5:
            self.type = "Five of A Kind"
        elif card_count[Card("J")] > 0:
            num_jokers = card_count[Card("J")]
            card_count.pop(Card("J"))
            if card_count.most_common()[0][1] + num_jokers == 5:
                self.type = "Five of A Kind"
            elif card_count.most_common()[0][1] + num_jokers == 4:
                self.type = "Four of A Kind"
            elif card_count.most_common()[0][1] + num_jokers == 3:
                if card_count.most_common()[1][1] == 2:
                    self.type = "Full House"
                else:
                    self.type = "Three of A Kind"
            elif card_count.most_common()[0][1] + num_jokers == 2:
                self.type = "One Pair"
            else:
                self.type = "High Card"
        else:
            if card_count.most_common()[0][1] == 4:
                self.type = "Four of A Kind"
            elif card_count.most_common()[0][1] == 3:
                if card_count.most_common()[1][1] == 2:
                    self.type = "Full House"
                else:
                    self.type = "Three of A Kind"
            elif card_count.most_common()[0][1] == 2:
                if card_count.most_common()[1][1] == 2:
                    self.type = "Two Pair"
                else:
                    self.type = "One Pair"
            else:
                self.type = "High Card"
        self.hand_value = type_values[self.type]

    def __eq__(self, other):
        return self.hand_value == other.hand_value

    def __lt__(self, other):
        if self.hand_value == other.hand_value:
            for card, card_other in zip(self.cards, other.cards):
                if card.value == card_other.value:
                    continue
                else:
                    return card.value < card_other.value
        else:
            return self.hand_value < other.hand_value


test_cards = [Card("Q"), Card("J"), Card("J"), Card("Q"), Card("2")]
test_hand = Hand(test_cards, 100)

test_cards_2 = [Card("K"), Card("J"), Card("3"), Card("4"), Card("J")]
test_hand_2 = Hand(test_cards_2, 100)


assert test_hand_2.type == "Three of A Kind"


def parse_hands(input_data):
    hands = []
    for line in input_data:
        cards_str, bid = line.split(" ")[0], line.split(" ")[1]
        cards = [Card(rank) for rank in cards_str]
        hands.append(Hand(cards, bid))
    return hands


def play_round(input_data):
    hands = parse_hands(input_data)
    hands.sort()
    rankings = [x for x in range(1, len(hands) + 1)]
    winnings = 0
    for rank, hand in zip(rankings, hands):
        winnings += rank * hand.bid
    return winnings


assert play_round(test_data) == test_result


with open("../input_data/07_Camel_Cards.txt", "r", encoding="utf-8") as file:
    input_data = file.read().strip().split("\n")

answer_2 = play_round(input_data)
print(answer_2)
