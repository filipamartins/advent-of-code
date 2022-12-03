import math


def read_file(filename):
    with open(filename, "r") as file:
        return file.read().split(",")


def part2(data):
    min_fuel = math.inf
    for i in range(min(data), max(data)):
        fuel = 0
        for n in data:
            fuel += (abs(n - i) * (1 + abs(n - i))) // 2
        min_fuel = min(fuel, min_fuel)
    return min_fuel


def part1(data):
    min_fuel = math.inf
    for i in range(min(data), max(data)):
        fuel = 0
        for n in data:
            fuel += abs(n - i)
        min_fuel = min(fuel, min_fuel)
    return min_fuel


if __name__ == "__main__":
    data = read_file("input.txt")
    data = [int(x) for x in data]
    print(part1(data))
    print(part2(data))
