def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input):
    coords_s, instructions = input.split("\n\n")

    coords = set()
    for line in coords_s.splitlines():
        x_s, y_s = line.split(",")
        coords.add((int(x_s), int(y_s)))
    return coords, instructions


def print_points(coords):
    max_x = max(x for x, _ in coords)
    max_y = max(y for _, y in coords)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1(coords, instructions):
    # only first fold
    # find the number of dots after the first fold
    # print_points(coords)
    for line in instructions.splitlines():
        instruc, num_s = line.split("=")
        axis = instruc[-1]
        num = int(num_s)

        if axis == "x":
            coords = {(x if x < num else (2 * num - x), y) for x, y in coords}
        else:
            # axis =y
            coords = {(x, y if y < num else (2 * num - y)) for x, y in coords}

        print(f"solution1: {len(coords)}")
        break


def part2(coords, instructions):
    for line in instructions.splitlines():
        instruc, num_s = line.split("=")
        axis = instruc[-1]
        num = int(num_s)

        if axis == "x":
            coords = {(x if x < num else (2 * num - x), y) for x, y in coords}
        else:
            # axis =y
            coords = {(x, y if y < num else (2 * num - y)) for x, y in coords}
    print_points(coords)


input_path = "day_13/input.txt"
test_input_path = "day_13/test_input.txt"

input = read_lines(input_path)
coords, instructions = parse_input(input)

coords2 = coords.copy()
# instructions2 = instructions.copy()

part1(coords, instructions)
part2(coords2, instructions)
