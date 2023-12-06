import re


def get_calibration_value(input_string: str) -> int:
    number_list = []
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        }
    string_length = len(input_string)
    for i, letter in enumerate(input_string):
        if letter in [str(x) for x in number_map.values()]:
            number_list.append(int(letter))
        elif i + 3 >= string_length:
            pass
        if i + 4 <= string_length:
            three_letter_number = input_string[i:i+3]
            if three_letter_number in number_map.keys():
                number_list.append(number_map[three_letter_number])
        if i + 5 <= string_length:
            four_letter_number = input_string[i:i+4]
            if four_letter_number in number_map.keys():
                number_list.append(number_map[four_letter_number])
        if i + 6 <= string_length:
            five_letter_number = input_string[i:i+5]
            if five_letter_number in number_map.keys():
                number_list.append(number_map[five_letter_number])
    return int(str(number_list[0]) + str(number_list[-1]))


def sum_calibration_values(input_list: list[str]) -> int:
    sum = 0
    for line in input_list:
        sum += get_calibration_value(line)
    return sum


if __name__ == "__main__":
    with open("prod_input.txt") as f:
        lines = f.readlines()
        print(sum_calibration_values(lines))
