def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def part1(data):
    hrz = depth = 0
    for line in data:
        d, n = line.split(" ")
        n = int(n)
        if d == "forward":
            hrz += n
        elif d == "up":
            depth -= n
        else:
            depth += n
    return hrz * depth


def part2(data):
    hrz = depth = aim = 0
    for line in data:
        d, n = line.split(" ")
        n = int(n)
        if d == "forward":
            hrz += n
            depth += aim * n
        elif d == "up":
            aim -= n
        else:
            aim += n
    return hrz * depth


if __name__ == "__main__":
    data = read_file("input.txt")
    print(part1(data))
    print(part2(data))
