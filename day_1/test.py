from . import part_1
from . import part_2


def test_get_calibration_value():
    actual = part_1.get_calibration_value("1abc2")
    assert actual == 12


def test_part_1():
    with open("test_input_1.txt") as f:
        lines = f.readlines()
        actual = part_1.sum_calibration_values(lines)
    expected = 142
    assert actual == expected


def test_part_2():
    with open("test_input_2.txt") as f:
        lines = f.readlines()
        actual = part_2.sum_calibration_values(lines)
    expected = 281
    assert actual == expected
