import math


def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(cave):
    cave = [list(x) for x in cave.split("\n")]
    # converting from str to int ß
    cave = [list(map(int, x)) for x in cave]
    return cave


def adjacent_points(cave, row, col):
    adj = []

    if row + 1 < len(cave):
        adj.append(cave[row + 1][col])

    if row - 1 >= 0:
        adj.append(cave[row - 1][col])

    if col + 1 < len(cave[0]):
        adj.append(cave[row][col + 1])

    if col - 1 >= 0:
        adj.append(cave[row][col - 1])

    return adj


def part1(cave):
    total = 0
    for row in range(len(cave)):
        for col in range(len(cave[0])):
            ad = adjacent_points(cave, row, col)
            if cave[row][col] < min(ad):
                total += 1 + cave[row][col]

    print(f"solution1: {total}")


def basin_count(row, col, cave, basin_size):
    if (
        row < 0
        or row >= len(cave)
        or col < 0
        or col >= len(cave[0])
        or cave[row][col] == 9
        or cave[row][col] == -1
    ):
        return
    cave[row][col] = -1
    basin_size[len(basin_size) - 1] += 1
    basin_count(row + 1, col, cave, basin_size)
    basin_count(row - 1, col, cave, basin_size)
    basin_count(row, col + 1, cave, basin_size)
    basin_count(row, col - 1, cave, basin_size)


def part2(cave):
    basin_size = []
    low_points = []

    for row in range(len(cave)):
        for col in range(len(cave[0])):
            if cave[row][col] < min(adjacent_points(cave, row, col)):
                low_points.append((row, col))

    for row, col in low_points:
        basin_size.append(0)
        basin_count(row, col, cave, basin_size)

    # print(f"basin size: {basin_size}")
    print(f"solution2: {math.prod(sorted(basin_size, reverse=True)[:3])}")


input_path = "day_9/input.txt"
test_input_path = "day_9/test_input.txt"
input = read_input(input_path)
cave = parse_input(input)
cave2 = cave.copy()
part1(cave)
part2(cave2)
