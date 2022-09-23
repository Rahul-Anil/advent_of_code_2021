literal = []
input = "101111111000101000"
for i in range(0, len(input) - 5, 5):
    if input[i] == 0:
        literal.append(input[i + 1 : i + 5])
        break
    literal.append(input[i + 1 : i + 5])

literal_s = "".join(literal)
assert literal_s == "011111100101", f"actual: 011111100101\ngot: {literal_s}"
assert int(literal_s, 2) == 2021
