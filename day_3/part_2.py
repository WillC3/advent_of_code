def get_coordinates(
    lines: list[str],
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """
    Returns a list of number_coordinates and a list of symbol coordinates.
    """
    number_coords = []
    symbol_coords = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in "0123456789":
                number_coords.append((i, j))
            elif char == "*":
                symbol_coords.append((i, j))
    return (number_coords, symbol_coords)


def get_gear_numbers(
    number_coords: list[tuple[int, int]], symbol_coords: list[tuple[int, int]]
) -> set[tuple[int, int]]:
    answer_set = set()
    for coord in symbol_coords:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                check_coord = (coord[0] + i, coord[1] + j)
                if check_coord in number_coords:
                    answer_set.add(check_coord)
    return answer_set


def create_coord_ranges(
    number_coords: list[tuple[int, int]],
) -> list[tuple[int, list[int]]]:
    ranges = []
    number_coords_local: list[tuple[int, int]] = number_coords.copy()
    while number_coords_local != []:
        coord_range: tuple[int, list[int]] = [
            number_coords_local[0][0],
            [number_coords_local[0][1]],
        ]
        number_coords_local.pop(0)
        if number_coords_local == []:
            break
        while list(number_coords_local[0]) == [coord_range[0], coord_range[1][-1] + 1]:
            coord_range[1].append(coord_range[1][-1] + 1)
            number_coords_local.pop(0)
            if number_coords_local == []:
                break
        ranges.append(tuple(coord_range))
    return ranges


def get_number_ranges(
    ranges: list[list[int, list[int]]],
    parts: set[tuple[int, int]],
) -> list[list[int, list[int]]]:
    target_number_coords = []
    for coord in parts:
        for range in ranges:
            if coord[0] == range[0]:
                if coord[1] in range[1]:
                    if range not in target_number_coords:
                        target_number_coords.append(range)
    return target_number_coords


def sum_numbers_from_ranges(lines: str, ranges: list[list[int, list[int]]]) -> int:
    answer = 0
    answer_list = []
    for range in ranges:
        num_string = ""
        for i in range[1]:
            num_string += lines[range[0]][i]
        answer += int(num_string)
        answer_list.append(num_string)
    return answer


def final_answer(lines: str) -> int:
    number_coords, symbol_coords = get_coordinates(lines)
    parts = get_part_numbers(number_coords, symbol_coords)
    ranges = create_coord_ranges(number_coords)
    answer_ranges = get_number_ranges(ranges, parts)
    answer = sum_numbers_from_ranges(lines, answer_ranges)
    return answer


if __name__ == "__main__":
    with open("prod_input.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
        answer = final_answer(lines)
 
