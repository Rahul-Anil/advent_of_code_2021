def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input):
    check = []
    octo_energy = {}
    for row, line in enumerate(input.splitlines()):
        for col, c in enumerate(line):
            octo_energy[row, col] = int(c)
            # check[row][col] = int(c)

    return octo_energy


def adj_points(x, y):
    for x_d in (-1, 0, 1):
        for y_d in (-1, 0, 1):
            if x_d == y_d == 0:
                continue
            yield x + x_d, y + y_d


def part1(octo_energy):
    flashes = 0
    for _ in range(100):
        octo_full = []
        for k, v in octo_energy.items():
            octo_energy[k] += 1
            if octo_energy[k] > 9:
                octo_full.append(k)

        while octo_full:
            o = octo_full.pop()

            # check if the point has already flashed
            if octo_energy[o] == 0:
                continue

            octo_energy[o] = 0
            flashes += 1

            # need to increment points around the cuurent coordinate
            for adj in adj_points(*o):
                if adj in octo_energy and octo_energy[adj] != 0:
                    octo_energy[adj] += 1
                    if octo_energy[adj] > 9:
                        octo_full.append(adj)

    print(f"flashes: {flashes}")


def part2(octo_energy):
    step = 0
    while True:
        step += 1
        octo_full = []
        for k, v in octo_energy.items():
            octo_energy[k] += 1
            if octo_energy[k] > 9:
                octo_full.append(k)

        while octo_full:
            o = octo_full.pop()

            # check if the point has already flashed
            if octo_energy[o] == 0:
                continue

            octo_energy[o] = 0

            # need to increment points around the cuurent coordinate
            for adj in adj_points(*o):
                if adj in octo_energy and octo_energy[adj] != 0:
                    octo_energy[adj] += 1
                    if octo_energy[adj] > 9:
                        octo_full.append(adj)

        if all(val == 0 for val in octo_energy.values()):
            break

    print(f"solution2: {step}")


input_path = "day_11/input.txt"
test_input_path = "day_11/test_input.txt"
small_example_test_input_path = "day_11/small_test_example.txt"

input = read_lines(input_path)
octo_energy = parse_input(input)
octo_energy2 = octo_energy.copy()

part1(octo_energy)
part2(octo_energy2)
