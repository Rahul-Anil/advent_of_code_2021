def read_input(path):
    with open(path) as f:
        lines = f.read()
    f.close()
    input_list = lines.split()
    input_list = list(map(int, input_list))
    return input_list


input_path = "day_1/input.txt"
input = read_input(input_path)
test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

icr = 0

for i in range(3, len(input)):
    if input[i - 3] < input[i]:
        icr += 1

print(icr)
