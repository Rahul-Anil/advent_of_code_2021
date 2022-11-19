def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(crab_pos):
    crab_pos = [int(c) for c in crab_pos.split(",")]
    return crab_pos


def fuel_used_2(pos, crab_pos):
    fuel_used = 0
    for c in crab_pos:
        n = abs(pos - c)
        fuel_used += (n * (n + 1)) / 2
    return fuel_used


def fuel_used(pos, crab_pos):
    fuel_used = 0
    for c in crab_pos:
        fuel_used += abs(pos - c)
    return fuel_used


def part1(crab_pos):
    min_crab_pos = min(crab_pos)
    max_crab_pos = max(crab_pos)
    crab = {}
    for p in range(min_crab_pos, max_crab_pos):
        crab[p] = fuel_used(p, crab_pos)
    pos = {key: value for key, value in crab.items() if value == (min(crab.values()))}
    print(f"solution 1: {pos}")
    return pos


def part2(input):
    min_crab_pos = min(crab_pos)
    max_crab_pos = max(crab_pos)
    crab = {}
    for p in range(min_crab_pos, max_crab_pos):
        crab[p] = fuel_used_2(p, crab_pos)
    pos = {key: value for key, value in crab.items() if value == (min(crab.values()))}
    print(f"solution 2: {pos}")
    return pos


test_input_path = "day_7/test_input.txt"
input_path = "day_7/input.txt"
input = read_input(input_path)
crab_pos = parse_input(input)
crab_pos_2 = crab_pos.copy()

solution1 = part1(crab_pos)
solution2 = part2(crab_pos)
