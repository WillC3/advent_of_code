def get_calibration_value(input_string: str) -> int:
    number_list = []
    for letter in input_string:
        try:
            number_list.append(int(letter))
        except Exception:
            pass
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
