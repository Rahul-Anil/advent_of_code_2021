import heapq


def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines


def adj_points(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def parse_input(input):
    coords = {}
    for x, line in enumerate(input.splitlines()):
        for y, col in enumerate(line):
            coords[(x, y)] = int(col)

    return coords


def part1(coords):
    # need to convert my input to the form of an adj matrix so i can use the
    # dijk algorithm for solving this problem
    goal_x, goal_y = max(coords)

    # solving using dijk algorithm using priority queues
    best_at = {(0, 0): 0}

    # start at the left most corner
    todo = [(0, (0, 0))]

    while todo:
        cost, last_coords = heapq.heappop(todo)

        neighbours = []
        for cand in adj_points(*last_coords):
            if cand in coords:
                neighbours.append(cand)

        if best_at[last_coords] < cost:
            continue
        for n in neighbours:
            new_dist = best_at[last_coords] + coords[(n[0], n[1])]

            if n not in best_at or new_dist < best_at[n]:
                best_at[n] = new_dist
                heapq.heappush(todo, (new_dist, n))

    print(f"solution1: {best_at[(goal_x, goal_y)]}")


def wrap(c):
    # if the wrap is greater than 9 then we need to subtract 9 from it to get
    # the actual number it will be
    while c > 9:
        c -= 9
    return c


def part2(input):
    coords = {}
    lines = input.splitlines()
    height = len(lines)
    width = len(lines[0])

    for x, line in enumerate(input.splitlines()):
        for y, risk in enumerate(line):
            for x_r in range(5):
                for y_r in range(5):
                    coords[(x_r * height + x, y_r * width + y)] = wrap(
                        int(risk) + x_r + y_r
                    )

    # print(f"coords: {coords}")
    part1(coords)


input_path = "day_15/input.txt"
test_input_path = "day_15/test_input.txt"
input = read_lines(input_path)
coords = parse_input(input)

part1(coords)
part2(input)
