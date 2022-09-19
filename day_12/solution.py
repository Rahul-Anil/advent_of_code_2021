import collections


def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input: str) -> collections.defaultdict:
    # representing the problem in the form of a graph using default dict
    # this will be a bidirectional graph
    edges = collections.defaultdict(set)
    for line in input.splitlines():
        source, destination = line.split("-")
        edges[source].add(destination)
        edges[destination].add(source)

    return edges


def part1(paths):
    # this then boils down to some form of searching over all paths in the graph
    all_paths = set()  # its a set so that we dont end up adding duplicate paths
    todo = [("start",)]

    while todo:
        path = todo.pop()

        if path[-1] == "end":
            all_paths.add(path)
            continue

        for cand in paths[path[-1]]:
            # if the candidate is upper or if the candidate is lower and not in path then we can add it to the todo again
            if not cand.islower() or cand not in path:
                todo.append((*path, cand))

    print(f"solution1: {len(all_paths)}")


def part2(paths):
    all_paths = set()
    todo = [(("start",), False)]

    while todo:
        path, lower_double_cave = todo.pop()

        if path[-1] == "end":
            all_paths.add(path)
            continue

        for cand in paths[path[-1]]:
            # if start then stop
            if cand == "start":
                continue
            # if it is upper case or candidate has not been seen yet then add it to the todo list
            elif cand.isupper() or cand not in path:
                todo.append(((*path, cand), lower_double_cave))
            # if candidate is lower cas and it has already been visited before
            # and if lower_double_cave is False
            elif not lower_double_cave:
                todo.append(((*path, cand), True))

    print(f"solution2: {len(all_paths)}")


input_path = "day_12/input.txt"
test_input_path = "day_12/test_input.txt"
input = read_lines(input_path)
paths = parse_input(input)

part1(paths)
part2(paths)
