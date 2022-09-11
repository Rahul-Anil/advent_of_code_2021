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

oxy_data = input.copy()
co2_data = input.copy()

index = 0

while len(oxy_data) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []

    for i in range(len(oxy_data)):
        if oxy_data[i][index] == "0":
            zero += 1
            zeros.append(oxy_data[i])
        else:
            one += 1
            ones.append(oxy_data[i])

    if zero > one:
        oxy_data = zeros
    else:
        oxy_data = ones

    index += 1

print(f"oxy_data: {oxy_data}")

index = 0

while len(co2_data) > 1:
    one = 0
    zero = 0
    ones = []
    zeros = []

    for j in range(len(co2_data)):
        if co2_data[j][index] == "0":
            zero += 1
            zeros.append(co2_data[j])
        else:
            one += 1
            ones.append(co2_data[j])

    if one < zero:
        co2_data = ones
    else:
        co2_data = zeros

    index += 1

print(f"co2_data: {co2_data}")

print(f"final ans: {int(oxy_data[0],2)*int(co2_data[0],2)}")
