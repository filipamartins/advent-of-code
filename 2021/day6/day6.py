def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split(",")


def part1(data):
    new_data = data[:]
    for _ in range(80):
        new_fish = []
        for j in range(len(new_data)):
            if new_data[j] == 0:
                new_data[j] = 6
                new_fish.append(8)
            else:
                new_data[j] -= 1
        new_data.extend(new_fish)
    return len(new_data)


def part2(data):
    d = {}
    for age in data:
        d[age] = d.get(age, 0) + 1
    for i in range(256):
        aux_zero = d.get(0, 0)
        for i in range(1, 9):
            d[i - 1] = d.get(i, 0)
        d[8] = aux_zero
        d[6] = d.get(6, 0) + aux_zero

    return sum([value for value in d.values()])


if __name__ == "__main__":
    data = read_file("input.txt")
    data = [int(x) for x in data]
    print(part1(data))
    print(part2(data))
