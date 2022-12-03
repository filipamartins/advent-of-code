def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()


def part1(data):
    num = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            num += 1
    return num


def part2(data):
    num = 0
    for i in range(len(data) - 2):
        if sum(data[i + 1 : i + 4]) > sum(data[i : i + 3]):
            num += 1
    return num


if __name__ == "__main__":
    data = read_file("input.txt")
    data = [int(i) for i in data]
    print(part1(data))
    print(part2(data))
