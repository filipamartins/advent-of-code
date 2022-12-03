def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def get_low_points_info(data):
    low_points = []
    pos = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            x = data[i][j]
            l = data[i][j - 1]
            r = data[i][j + 1]
            u = data[i - 1][j]
            d = data[i + 1][j]
            if x < l and x < r and x < u and x < d:
                low_points.append(x)
                pos.append([i, j])
    return [low_points, pos]


def part1(data):
    low_points = get_low_points_info(data)[0]
    return sum(low_points) + 1 * len(low_points)


def find_basin_size(data, x, y, mark):
    if data[x][y] == 9:
        return 0
    elif mark[x][y] == 1:
        return 0
    mark[x][y] = 1
    result = 1
    result += find_basin_size(data, x, y - 1, mark)
    result += find_basin_size(data, x, y + 1, mark)
    result += find_basin_size(data, x - 1, y, mark)
    result += find_basin_size(data, x + 1, y, mark)
    return result


def part2(data):
    low_points_info = get_low_points_info(data)
    points_pos = low_points_info[1]
    sizes = []

    for pos in points_pos:
        mark = []
        for i in range(len(data)):
            lst = [0] * len(data[0])
            mark.append(lst)
        x, y = pos[0], pos[1]
        sizes.append(find_basin_size(data, x, y, mark))
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def parse_input(data):
    new_data = []
    for line in data:
        line = [int(x) for x in line]
        line = [9] + line + [9]
        new_data.append(line)
    nines = [9] * len(new_data[0])
    new_data.insert(0, nines)
    new_data.append(nines)
    return new_data


if __name__ == "__main__":
    data = read_file("input.txt")
    p_data = parse_input(data)
    print(part1(p_data))
    print(part2(p_data))
