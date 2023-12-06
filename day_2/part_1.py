def check_valid_game(game: dict[str, int], bag: dict[str, int]) -> bool:
    for colour in bag.keys():
        for turn in game:
            if colour in turn.keys():
                if bag[colour] < turn[colour]:
                    return False
    return True


def create_bag(red: int, green: int, blue: int) -> dict[str, int]:
    return {"red": red, "green": green, "blue": blue}


def prepare_line(line: str) -> list[int, dict[str, int]]:
    line = line.replace("\n", "")
    line = line.replace("Game ", "")
    line = line.split(":")
    game_id = int(line[0])
    game = line[1].strip()
    game = game.split(";")
    game = [x.replace(",", "").split() for x in game]
    for i, turn in enumerate(game):
        turn_dict = {}
        for j in range(0, len(turn), 2):
            turn_dict[turn[j+1]] = int(turn[j])
        game[i] = turn_dict

    return [game_id, game]


def sum_possible_game_ids(file: str, red: int, green: int, blue: int) -> int:
    bag = create_bag(red, green, blue)
    sum = 0
    for line in file:
        game = prepare_line(line)
        if check_valid_game(game[1], bag):
            sum += game[0]
    return sum


if __name__ == "__main__":
    with open("prod_input.txt") as f:
        lines = f.readlines()
        bag = create_bag(red=12, green=13, blue=14)
        print(sum_possible_game_ids(file = lines, red = 12, green = 13, blue = 14))
