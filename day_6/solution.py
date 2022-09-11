import numpy as np


def read_input(path):
    with open(path) as f:
        lines = f.read()
    return lines


def parse_input(input):
    fish = [int(f) for f in input.split(",")]
    fish_dict = {}
    for i in range(0, 9):
        fish_dict[i] = fish.count(i)
    return fish_dict


def dict_sum(input):
    sum = 0
    for i in range(9):
        sum += input[i]
    return sum


def part1(input):
    # print(f"input: {input}")
    day = 0
    while day < 80:
        day += 1
        temp = input[0]
        input[0] = 0
        for f in range(1, 9):
            input[f - 1] += input[f]
            input[f] = 0

        input[8] = temp
        input[6] += temp

    sum = dict_sum(input)
    print(f"sum part 1: {sum}")


def part2(input):
    day = 0
    while day < 256:
        day += 1
        temp = input[0]
        input[0] = 0
        for f in range(1, 9):
            input[f - 1] += input[f]
            input[f] = 0

        input[8] = temp
        input[6] += temp

    # print(f"dict: {input}")
    sum = dict_sum(input)
    print(f"sum part 2: {sum}")


test_input_path = "day_6/test_input.txt"
input_path = "day_6/input.txt"
input = read_input(input_path)
parsed_input = parse_input(input)
parsed_input_copy = parsed_input.copy()  # stupid copy
solution1 = part1(parsed_input)
solution2 = part2(parsed_input_copy)
