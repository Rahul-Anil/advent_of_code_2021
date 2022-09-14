def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(segment):
    left = []
    right = []
    segment = segment.split("\n")
    for s in segment:
        l, r = s.split("|")
        left.append(l.strip().split())
        right.append(r.strip().split())

    return (left, right)


def part2(left_segment, right_segment):
    sum = 0
    mappings = []

    # key:value : number of segments: number which has that many segments
    unq_seg = {2: 1, 3: 7, 4: 4, 7: 8}

    for l in left_segment:
        segment_mapping = {}

        # finding out the pattern for all the unq segments
        for pattern in l:
            if len(pattern) in unq_seg:
                segment_mapping[unq_seg[len(pattern)]] = pattern

        # 6 linked segments: 6,9,0
        # Finding 6
        for pattern in l:
            if len(pattern) == 6 and any(c not in pattern for c in segment_mapping[1]):
                segment_mapping[6] = pattern
                break

        # Finding 9
        for pattern in l:
            if (
                len(pattern) == 6
                and all(c in pattern for c in segment_mapping[4])
                and (pattern not in segment_mapping.values())
            ):
                segment_mapping[9] = pattern
                break

        # finding 0
        for pattern in l:
            if len(pattern) == 6 and (pattern not in segment_mapping.values()):
                segment_mapping[0] = pattern
                break

        # 5 linked segments: 2, 3, 5

        # finding 2
        for pattern in l:
            if len(pattern) == 5 and any(c not in segment_mapping[9] for c in pattern):
                segment_mapping[2] = pattern
                break

        # finding 3
        for pattern in l:
            if (
                len(pattern) == 5
                and all(c in pattern for c in segment_mapping[1])
                and (pattern not in segment_mapping.values())
            ):
                segment_mapping[3] = pattern
                break

        # finding 5
        for pattern in l:
            if len(pattern) == 5 and (pattern not in segment_mapping.values()):
                segment_mapping[5] = pattern

        mappings.append({v: k for k, v in segment_mapping.items()})

    total = 0
    for idx, r in enumerate(right_segment):
        num = []
        for pattern in r:
            for p in mappings[idx]:
                if all(char in p for char in pattern) and len(p) == len(pattern):
                    # print(f"pattern: {pattern}, p: {p}")
                    num.append(str(mappings[idx][p]))

        sum += int("".join(num))

    print(f"solution2: {sum}")


input_path = "day_8/input.txt"
test_input_path = "day_8/test_input.txt"
input = read_input(input_path)
left_segment, right_segment = parse_input(input)

part2(left_segment, right_segment)
