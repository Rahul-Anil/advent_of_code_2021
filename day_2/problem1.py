def read_input(path):
    with open(path) as f:
        lines = f.read()
    f.close()
    return lines


input_path = "day_2/input.txt"
input = read_input(input_path).split()

# input = [
#     "forward",
#     "5",
#     "down",
#     "5",
#     "forward",
#     "8",
#     "up",
#     "3",
#     "down",
#     "8",
#     "forward",
#     "2",
# ]

horizontal_pos = 0
depth_pos = 0

for i in range(0, len(input), 2):
    if input[i] == "forward":
        horizontal_pos += int(input[i + 1])
    elif input[i] == "down":
        depth_pos += int(input[i + 1])
    else:
        depth_pos -= int(input[i + 1])

print(f"Final position: {horizontal_pos*depth_pos}")
