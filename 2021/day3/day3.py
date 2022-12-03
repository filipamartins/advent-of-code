def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def get_bits_for_index(data, i):
    return [int(line[i]) for line in data]


def most_common_bit(bits):
    n = sum(bits)
    return "1" if n >= len(bits) / 2 else "0"


def O2_generator_rating(data):
    filtered = data
    for i in range(len(data[0])):
        if len(filtered) == 1:
            break
        temp = []
        bits = get_bits_for_index(filtered, i)
        bit = most_common_bit(bits)
        for num in filtered:
            if num[i] == bit:
                temp.append(num)
        filtered = temp
    return int(filtered[0], 2)


def CO2_scrubber_rating(data):
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        temp = []
        bits = get_bits_for_index(data, i)
        bit = most_common_bit(bits)
        for num in data:
            if num[i] != bit:
                temp.append(num)
        data = temp
    return int(data[0], 2)


def part1(data):
    gama = epsilon = ""
    for i in range(len(data[0])):
        bits = get_bits_for_index(data, i)
        if most_common_bit(bits) == "1":
            gama += "1"
            epsilon += "0"
        else:
            gama += "0"
            epsilon += "1"
    return int(gama, 2) * int(epsilon, 2)


def part2(data):
    O2_rate = O2_generator_rating(data)
    CO2_rate = CO2_scrubber_rating(data)
    return O2_rate * CO2_rate


if __name__ == "__main__":
    data = read_file("input.txt")
    print(part1(data))
    print(part2(data))
