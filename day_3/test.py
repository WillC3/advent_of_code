from . import part_1


def test_part_1():
    with open("test_input.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
        actual = part_1.final_answer(lines)
    expected = 4361
    assert actual == expected
