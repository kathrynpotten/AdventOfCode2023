test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip().split(
    "\n"
)

test_result = 8


class RevealedSet:
    def __init__(self, colours):
        self.colours = colours
        self.red = [
            int(colour.split("red")[0]) for colour in colours if "red" in colour
        ]
        if self.red == []:
            self.red = 0
        else:
            self.red = self.red[0]
        self.blue = [
            int(colour.split("blue")[0]) for colour in colours if "blue" in colour
        ]
        if self.blue == []:
            self.blue = 0
        else:
            self.blue = self.blue[0]
        self.green = [
            int(colour.split("green")[0]) for colour in colours if "green" in colour
        ]
        if self.green == []:
            self.green = 0
        else:
            self.green = self.green[0]

    def __repr__(self):
        return f"RevealedSet({self.colours})"

    def __str__(self):
        return f"{self.red} red, {self.blue} blue, {self.green} green"


class Game:
    def __init__(self, ID):
        self.ID = ID
        self.revealed_sets = []

    def __repr__(self):
        return f"Game([{self.revealed_sets}])"

    def __str__(self):
        return (
            "Game"
            + str(self.ID)
            + ":"
            + "\n"
            + "\n".join(str(revealed_set) for revealed_set in self.revealed_sets)
        )

    def __iter__(self):
        return iter(self.revealed_sets)

    def add_set(self, *args):
        self.revealed_sets.extend(*args)

    def is_possible(self, red, green, blue):
        for revealed_set in self.revealed_sets:
            if revealed_set.red > red:
                return False
            elif revealed_set.green > green:
                return False
            elif revealed_set.blue > blue:
                return False
        return True


def parse_game(games_input):
    games = []
    for game in games_input:
        ID = int(game.split(":")[0].split(" ")[-1])
        new_game = Game(ID)
        sets = game.split(":")[1].split(";")
        for revealed_set in sets:
            colours = revealed_set.replace(" ", "").split(",")
            new_game.add_set([RevealedSet(colours)])
        games.append(new_game)
    return games


test_game_input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]

test_game = Game(1)
test_game.add_set(
    [
        RevealedSet(["3blue", "4red"]),
        RevealedSet(["1red", "2green", "6blue"]),
        RevealedSet(["2green"]),
    ]
)

assert repr(parse_game(test_game_input)[0]) == repr(test_game)
assert str(parse_game(test_game_input)[0]) == str(test_game)


def sum_of_possible_IDs(games, red, green, blue):
    sum = 0
    for game in games:
        if game.is_possible(red, green, blue):
            sum += game.ID
    return sum


test_games = parse_game(test_data)
assert sum_of_possible_IDs(test_games, 12, 13, 14) == test_result

with open("../input_data/02_Cube_Conundrum.txt", "r", encoding="utf-8") as file:
    input = file.read().strip().split("\n")

input_games = parse_game(input)
answer_1 = sum_of_possible_IDs(input_games, 12, 13, 14)
print(answer_1)
