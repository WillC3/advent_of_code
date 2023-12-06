def get_game_power(game: dict[str, int]) -> int:
    initial_bag = create_bag(0, 0, 0)
    for colour in initial_bag.keys():
        for turn in game:
            if colour in turn.keys():
                if turn[colour] > initial_bag[colour]:
                    initial_bag[colour] = turn[colour]
    power = initial_bag["red"]*initial_bag["green"]*initial_bag["blue"]
    return power


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


def sum_possible_game_ids(file: str) -> int:
    sum = 0
    for line in file:
        game = prepare_line(line)
        sum += get_game_power(game[1])
    return sum


if __name__ == "__main__":
    with open("prod_input.txt") as f:
        lines = f.readlines()
        print(sum_possible_game_ids(file=lines))
