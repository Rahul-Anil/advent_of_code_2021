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


def part1(left_segment, right_segment):
    unq_seg = {1: 0, 4: 0, 7: 0, 8: 0}
    for i in right_segment:
        for j in i:
            if len(j) == 2:
                unq_seg[1] += 1
            elif len(j) == 3:
                unq_seg[7] += 1
            elif len(j) == 4:
                unq_seg[4] += 1
            elif len(j) == 7:
                unq_seg[8] += 1

    sum = 0
    for s in unq_seg.values():
        sum += s

    print(f"solution 1: {sum}")


def part2(left_segment, right_segment):
    sum = 0
    mappings = []
    # unique segments
    unq_seg = {2: 1, 3: 7, 4: 4, 7: 8}
    for i in left_segment:

        segment_mapping = {}
        # finding out what combinations make unique segments

        # here i find the segment mappings for 1,4,7,8
        for j in i:
            if len(j) in unq_seg:
                segment_mapping[unq_seg[len(j)]] = "".join(sorted(j))

            # finding out the segment mappings for segments of length 6
            # 6, 9, 0
        for j in i:
            # finding 6: 7 is completely contained in 9 and 0 so exception is 6
            if len(j) == 6 and any(char not in j for char in segment_mapping[1]):
                segment_mapping[6] = "".join(sorted(j))
                break

        for j in i:
            # finding 0: 4 is completely contained in 9
            if (
                len(j) == 6
                and any(char in j for char in segment_mapping[4])
                and j not in segment_mapping.values()
            ):
                segment_mapping[0] = "".join(sorted(j))
                break

        for j in i:
            # finding 9: leftover
            if len(j) == 6 and j not in segment_mapping.values():
                segment_mapping[9] = "".join(sorted(j))
                break

        # finding out the segment mapping for segments of length 5
        # 2, 3, 5

        for j in i:
            # finding 5: 1 is only completely contained in 3
            if len(j) == 5 and all(char in segment_mapping[6] for char in j):
                segment_mapping[5] = "".join(sorted(j))
                break

        for j in i:
            # finding 3: 9 is completely contained in 3
            if (
                len(j) == 5
                and all(char in segment_mapping[9] for char in j)
                and j not in segment_mapping.values()
            ):
                segment_mapping[3] = "".join(sorted(j))
                break

        for j in i:
            # finding 2: leftover
            if len(j) == 5 and j not in segment_mapping.values():
                segment_mapping[2] = "".join(sorted(j))

        # print(f"segment_mappings: {segment_mapping}")
        # key value pair to value key pair
        mappings.append({v: k for k, v in segment_mapping.items()})

    # print(f"mappings: {mappings[0]}")
    # print(f"mappings: \n{mappings}")
    for i, j in enumerate(right_segment):
        num = []
        for x in j:
            print(f"i:{i}")
            print(mappings[i])
            num.append(mappings[i]["".join(sorted(x))])
        print(f"num: {num}")
        # print(num)

    print(f"solution 2: {sum}")
    return sum


input_path = "day_8/input.txt"
test_input_path = "day_8/test_input.txt"
input = read_input(test_input_path)
left_segment, right_segment = parse_input(input)

left_seg2 = left_segment.copy()
right_seg2 = right_segment.copy()

part1(left_segment, right_segment)
part2(left_seg2, right_seg2)
