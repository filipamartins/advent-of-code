from collections import defaultdict
import re


def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def sign_m_line(x1, x2, y1, y2):
    return 1 if (y2 - y1) / (x2 - x1) > 0 else -1


def part1_2(data):
    d = defaultdict(dict)
    for line in data:
        x1, y1, x2, y2 = re.findall(r"(\d+)", line)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            max_y = max(y1, y2)
            min_y = min(y1, y2)
            for i in range(min_y, max_y + 1):
                d[x1][i] = d[x1].get(i, 0) + 1
        elif y1 == y2:
            max_x = max(x1, x2)
            min_x = min(x1, x2)
            for i in range(min_x, max_x + 1):
                d[i][y1] = d[i].get(y1, 0) + 1
        # ----comment for part 1 --------------------------
        else:
            max_x, min_x = max(x1, x2), min(x1, x2)
            max_y, min_y = max(y1, y2), min(y1, y2)
            if sign_m_line(x1, x2, y1, y2) == 1:
                for i in range(min_x, max_x + 1):
                    d[i][min_y] = d[i].get(min_y, 0) + 1
                    min_y += 1
            else:
                for i in range(min_x, max_x + 1):
                    d[i][max_y] = d[i].get(max_y, 0) + 1
                    max_y -= 1
        # ----comment for part 1 ---------------------------
    return sum([1 for x in d for y in d[x] if d[x][y] > 1])


if __name__ == "__main__":
    data = read_file("input.txt")
    print(part1_2(data))
