x1, y1 = 0, 0
x2, y2 = 8, 8

x_min = min(x1, x2)
x_max = max(x1, x2)
y_min = min(y1, y2)
y_max = max(y1, y2)

l = []

for i in range(x_min, x_max + 1):
    for j in range(y_min, y_max + 1):
        if x2 != i:
            if (y2 - j) / (x2 - i) == 1 or (y2 - j) / (x2 - i) == 1:
                if (i, j) != (x1, y1) and (i, j) != (x2, y2):
                    l.append([i, j])

print(l)
