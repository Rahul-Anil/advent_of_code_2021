from tkinter import W


def read_input(path):
    with open(path) as f:
        lines = f.read()
    f.close()
    return lines


input_path = "day_3/input.txt"
input = read_input(input_path).split()

# input = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010",
# ]

gamma = [0] * len(input[0])
epsilon = [1] * len(input[0])

pos_sum = [0] * len(input[0])

for i in range(len(input)):
    for j in range(len(input[0])):
        pos_sum[j] += int(input[i][j])

for k in range(len(pos_sum)):
    if pos_sum[k] > (len(input) / 2):
        gamma[k] = 1
        epsilon[k] = 0
    else:
        gamma[k] = 0
        epsilon[k] = 1

print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")

gamma = "".join(map(str, gamma))
epsilon = "".join(map(str, epsilon))

print(f"gamma: {int(gamma,2)}")
print(f"epsilon: {int(epsilon,2)}")

power_con = int(gamma, 2) * int(epsilon, 2)
print(f"power_con: {power_con}")
