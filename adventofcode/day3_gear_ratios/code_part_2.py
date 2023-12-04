from collections import defaultdict

part_one_invalid_neighbors = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

def get_directions(x, y):
    top_left = (x - 1, y - 1)
    top = (x, y - 1)
    top_right = (x + 1, y - 1)
    right = (x + 1, y)
    bottom_right = (x + 1, y + 1)
    bottom = (x, y + 1)
    bottom_left = (x - 1, y + 1)
    left = (x - 1, y)
    return [top_left, top, top_right, right, bottom_right, bottom, bottom_left, left]

def is_valid_part_number(schematic: dict, coordinates: tuple) -> bool:
    for direction in get_directions(coordinates[0], coordinates[1]):
        if schematic[direction] not in part_one_invalid_neighbors:
            return True
    return False


def create_schematic_dict(problem_input: list[str]) -> dict:
    schematic_dict = defaultdict(str)
    for y_coord, line in enumerate(problem_input):
        for x_coord, char in enumerate(line):
            schematic_dict[(x_coord, y_coord)] = char
    return schematic_dict


part_two_valid_number_coordinates = []


def create_number(numbers_and_coordinates: list) -> int:
    number = ""
    coordinates = []
    for digit in numbers_and_coordinates:
        number += digit[1]
        coordinates.append(digit[0])
    part_two_valid_number_coordinates.append((coordinates, int(number)))
    return int(number)


def get_part_number_list(schematic: dict, columns: int, rows: int) -> list[int]:
    valid_part_numbers = []
    potential_part_numbers = []
    for i in range(rows):
        number_collector = []
        for j in range(columns + 1):
            if schematic[(j, i)] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                number_collector.append(((j, i), schematic[j, i]))
            else:
                potential_part_numbers.append(number_collector.copy())
                number_collector.clear()
    # now check those numbers
    for number_list in potential_part_numbers:
        for coordinate_number in number_list:
            if is_valid_part_number(schematic, (coordinate_number[0][0], coordinate_number[0][1])):
                valid_part_numbers.append(create_number(number_list))
                break
    return valid_part_numbers


def get_asterisk_coordinates(schematic: dict, columns: int, rows: int) -> list[tuple]:
    asterisk_coordinates = []
    for i in range(rows):
        for j in range(columns + 1):
            if schematic[(j, i)] == "*":
                asterisk_coordinates.append((j, i))
    return asterisk_coordinates

def get_gear_ratios(asterisks: list) -> list[int]:
    gear_ratios = []
    for asterisk in asterisks:
        multiplicators = set()
        for direction in get_directions(asterisk[0], asterisk[1]):
            for number_info in part_two_valid_number_coordinates:
                if direction in number_info[0]:
                    multiplicators.add(number_info[1])
                if len(multiplicators) == 2:
                    break
        if len(multiplicators) == 2:
            mult_list = list(multiplicators)
            gear_ratios.append(mult_list[0] * mult_list[1])
            multiplicators.clear()
        else:
            multiplicators.clear()
    return gear_ratios


if __name__ == '__main__':
    lines = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    f.closed
    data = defaultdict(str)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            data[(j, i)] = char

    part_numbers = get_part_number_list(data, len(lines[0]), len(lines))
    asterisk_locations = get_asterisk_coordinates(data, len(lines[0]), len(lines))
    the_gear_ratios = get_gear_ratios(asterisk_locations)
    print(f"Sum of gear ratios is {sum(the_gear_ratios)}")