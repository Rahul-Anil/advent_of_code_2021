import collections


def read_lines(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input):
    template, rules_s = input.split("\n\n")
    rules = {}
    for r in rules_s.splitlines():
        left, right = r.split(" -> ")
        rules[left] = right
    return template, rules


# slow solution
def part1(template, rules):
    for _ in range(10):
        new_template = []
        for i in range(len(template) - 1):
            if template[i : i + 2] in rules:
                new_template.append(template[i] + rules[template[i : i + 2]])
            else:
                new_template.append(template[i : i + 2])
        template = "".join(new_template) + template[-1]
        # print(f"{template=}")

    char_count = collections.Counter(template)
    vals = sorted(char_count.values())
    print(f"solution1: {vals[-1] - vals[0]}")


# fast solution
def part2(template, rules):
    # find all the initial pairs in the template
    pair_counts = collections.Counter()
    for i in range(0, len(template) - 1):
        pair_counts[template[i : i + 2]] += 1

    for _ in range(40):
        new_counts = collections.Counter()
        for k, v in pair_counts.items():
            # because we are counting the number this way we need to add both the pairs
            new_counts[f"{k[0]}{rules[k]}"] += v
            new_counts[f"{rules[k]}{k[1]}"] += v
        pair_counts = new_counts

    char_count = collections.Counter()
    for k, v in pair_counts.items():
        # we only need to count the starting one of each one otherwise
        # we end up counting the same letter twice
        char_count[k[0]] += v
    char_count[template[-1]] += 1

    print(f"solution2: {max(char_count.values()) - min(char_count.values())}")


input_path = "day_14/input.txt"
test_input_path = "day_14/test_input.txt"
input = read_lines(input_path)
template, rules = parse_input(input)
template2, rules2 = template, rules.copy()

part1(template, rules)
part2(template, rules)
