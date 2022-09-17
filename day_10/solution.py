def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(coords):
    coords = coords.split("\n")
    return coords


def invalid_bracket(line):
    open_close = {"{": "}", "(": ")", "[": "]", "<": ">"}
    open_brackets = ["{", "(", "[", "<"]
    open = []
    for b in line:
        if b in open_brackets:
            open.append(b)
        else:
            if b != open_close[open[-1]] or len(open) == 0:
                return b
            else:
                open.pop(-1)


def point_count(invalid_elements):
    # print(f"invalid elements: {invalid_elements}")
    point_dict = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}
    total = 0
    for i in invalid_elements:
        total += point_dict[i]
    return total


def part1(coords):
    invalid_element = []
    for line in coords:
        invalid_element.append(invalid_bracket(line))

    solution1 = point_count(invalid_element)
    print(f"solution1: {solution1}")


def autocomplete_score(complete):
    total = 0
    score_dict = {")": 1, "]": 2, "}": 3, ">": 4}
    for i in range(len(complete)):
        total = (total * 5) + score_dict[complete[i]]
    return total


def complete_line(line):
    open_close = {"{": "}", "(": ")", "[": "]", "<": ">"}
    open_brackets = ["{", "(", "[", "<"]
    open = []
    complete = []
    for b in line:
        if b in open_brackets:
            open.append(b)
        else:
            if b == open_close[open[-1]]:
                open.pop(-1)

    for b in reversed(open):
        complete.append(open_close[b])

    score = autocomplete_score(complete)
    return score


def is_valid(line):
    open_close = {"{": "}", "(": ")", "[": "]", "<": ">"}
    open_brackets = ["{", "(", "[", "<"]
    open = []
    for b in line:
        if b in open_brackets:
            open.append(b)
        else:
            if b != open_close[open[-1]] or len(open) == 0:
                return False
            else:
                open.pop(-1)
    return True


def part2(coords):
    incomplete_coords = []
    bracket_complete = []
    line_score = []
    for line in coords:
        if is_valid(line):
            incomplete_coords.append(line)

    for line in incomplete_coords:
        line_score.append(complete_line(line))

    line_score.sort()
    middle_element = len(line_score) // 2
    print(f"solution2: {line_score[middle_element]}")


input_path = "day_10/input.txt"
test_input_path = "day_10/test_input.txt"
invalid_input_path = "day_10/invalid_input_check.txt"

input = read_input(input_path)
coords = parse_input(input)
coords2 = coords.copy()

part1(coords)
part2(coords)
