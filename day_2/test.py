from . import part_1
from . import part_2


def test_part_1():
    with open("test_input.txt") as f:
        lines = f.readlines()
        actual = part_1.sum_possible_game_ids(
            file=lines,
            red=12,
            green=13,
            blue=14)
    expected = 8
    assert actual == expected


def test_part_2():
    with open("test_input.txt") as f:
        lines = f.readlines()
        actual = part_2.sum_possible_game_ids(lines)
    expected = 2286
    assert actual == expected
