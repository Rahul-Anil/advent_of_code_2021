import statistics


def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input):
    return input.splitlines()


def part1(coords):
    FORWARD = {"{": "}", "(": ")", "[": "]", "<": ">"}
    REVERSE = {v: k for k, v in FORWARD.items()}

    point_count = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0

    for line in coords:
        open_brackets = []
        for b in line:
            if b in FORWARD:
                open_brackets.append(b)
            elif b in REVERSE:
                if REVERSE[b] == open_brackets[-1]:
                    open_brackets.pop()
                else:
                    total += point_count[b]
                    break

    print(f"solution1: {total}")


def part2(coords):
    FORWARD = {"{": "}", "(": ")", "[": "]", "<": ">"}
    REVERSE = {v: k for k, v in FORWARD.items()}

    point_count = {")": 1, "]": 2, "}": 3, ">": 4}
    points = []

    for line in coords:
        open_brackets = []
        for b in line:
            if b in FORWARD:
                open_brackets.append(b)
            elif b in REVERSE:
                if REVERSE[b] == open_brackets[-1]:
                    open_brackets.pop()
                else:
                    # total += point_count[b]
                    break

        # this else loop will run only when the for loop has been completely finished
        else:
            total = 0
            # the open_brackets here will contain all the brackets that need to be closed
            for b in reversed(open_brackets):
                total *= 5
                total += point_count[FORWARD[b]]
            points.append(total)

    print(f"solution1: {statistics.median(points)}")


input_path = "day_10/input.txt"
test_input_path = "day_10/test_input.txt"
invalid_input_path = "day_10/invalid_input_check.txt"

input = read_input(input_path)
coords = parse_input(input)
coords2 = coords.copy()

part1(coords)
part2(coords2)
