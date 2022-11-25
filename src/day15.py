import heapq


def adjPoints(x, y):
    yield x, y + 1
    yield x + 1, y
    yield x, y - 1
    yield x - 1, y


def pathFinder(coords: dict[(int, int), int]) -> int:
    goal = max(coords)
    todo = [(0, (0, 0))]
    dists = {(0, 0): 0}

    while todo:
        risk, curr = heapq.heappop(todo)

        neigh = []
        for n in adjPoints(*curr):
            if n in coords:
                neigh.append(n)

        for n in neigh:
            newDist = dists[curr] + coords[n]

            if n not in dists or newDist < dists[n]:
                dists[n] = newDist
                heapq.heappush(todo, (newDist, n))

    return dists[goal]


def part1(input: str) -> int:
    coords: dict[(int, int), int] = {}
    for x, rows in enumerate(input.splitlines()):
        for y, val in enumerate(rows):
            coords[(x, y)] = int(val)

    return pathFinder(coords)


def wrap(x):
    if x > 9:
        x -= 9
    return x


def part2(input: str) -> int:
    lines = input.splitlines()
    height = len(lines)
    width = len(lines[0])

    coords: dict[(int, int), int] = {}
    for x, row in enumerate(input.splitlines()):
        for y, val in enumerate(row):
            for xr in range(5):
                for yr in range(5):
                    coords[(x + xr * height, y + yr * width)] = wrap(int(val) + xr + yr)

    return pathFinder(coords)


if __name__ == "__main__":
    with open("../tests/sample_inputs/day_15_sample.txt") as f:
        lines = f.read()
    print(part1(lines))
    print(part2(lines))
