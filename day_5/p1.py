import numpy as np


def read_input(path):
    with open(path) as f:
        lines = f.read()
    f.close()
    return lines


def input_to_list(input):
    coords_list = []

    for i in range(len(input)):
        a, b = input[i].split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        x1, y1 = int(x1), int(y1)
        x2, y2 = int(x2), int(y2)

        # append the values that i am going to use to create the intersection matrix

        if x1 == x2 or y1 == y2:
            # if the x coords are equal
            if x1 == x2:
                low = min(y1, y2)
                high = max(y1, y2)
                for i in range(low, high + 1):
                    coords_list.append([x1, i])

            # if y coords are equal
            if y1 == y2:
                low = min(x1, x2)
                high = max(x1, x2)
                for i in range(low, high + 1):
                    coords_list.append([i, y1])

    return coords_list


def intercept_count(coords, x_min, x_max, y_min, y_max):
    vents = np.zeros((x_max + 1, y_max + 1))
    # print(vents)

    for i, j in coords:
        vents[i][j] += 1

    print(vents.transpose())
    count = (vents >= 2).sum()
    return count


input_path = "day_5/input.txt"
test_input_path = "day_5/test_input.txt"
input = read_input(test_input_path).split("\n")

coords = input_to_list(input)
# print(f"coords: {coords}")

x_min = min(coords, key=lambda i: i[0])[0]
x_max = max(coords, key=lambda i: i[0])[0]
y_min = min(coords, key=lambda i: i[1])[1]
y_max = max(coords, key=lambda i: i[1])[1]

count = intercept_count(coords, x_min, x_max, y_min, y_max)
print(f"count: {count}")
