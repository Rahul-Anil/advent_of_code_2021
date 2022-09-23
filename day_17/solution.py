def parse_input(input):
    _, _, x_s, y_s = input.split()
    x_s = x_s[2:-1]
    y_s = y_s[2:]
    x1, x2 = list(map(int, x_s.split("..")))
    y1, y2 = list(map(int, y_s.split("..")))
    return (x1, x2, y1, y2)


def solution(x1, x2, y1, y2):
    # starting position is (0,0)
    # initial (x,y) velocity are not known

    # x position increases by its x velocity
    # y position increases by its y velocity
    # x decreases by one at each step till 0
    # y the probes y velocity decreases by 1 at each

    max_y = 0
    count = 0

    # why am i only brute force searching this range
    for y in range(y1, abs(y1)):
        for x in range(1, x2 + 1):
            v_x, v_y = x, y
            x_p = y_p = 0

            # this is to find the point that was reached in the highest point in its arc
            max_y_path = 0
            # this is simulating the path of the obj
            for t in range(2 * abs(y1) + 2):
                x_p += v_x
                y_p += v_y
                v_x = max(v_x - 1, 0)
                v_y -= 1

                max_y_path = max(max_y_path, y_p)

                # check if we hit
                if x1 <= x_p <= x2 and y1 <= y_p <= y2:
                    max_y = max(max_y, max_y_path)
                    count += 1
                    break
                elif x_p > x2 or y_p < y1:
                    break

    print(f"solution1: {max_y}")
    print(f"solution2: {count}")


input = "target area: x=144..178, y=-100..-76"
test_input = "target area: x=20..30, y=-10..-5"
x1, x2, y1, y2 = parse_input(input)
solution(x1, x2, y1, y2)
