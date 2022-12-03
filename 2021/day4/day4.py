def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


class BingoBoard:
    def __init__(self, board=None):
        self.board = board or []
        self.bingo = False

    def add_row(self, row):
        self.board.append(row)

    def get_column(self, i):
        return [row[i] for row in self.board]

    def mark_number(self, n):
        for row in self.board:
            if n in row:
                i = row.index(n)
                row[i] = "x"
                column = self.get_column(i)
                if row.count("x") == len(row) or column.count("x") == len(column):
                    self.bingo = True

    def count_board(self, called_number):
        s = 0
        for row in self.board:
            for n in row:
                if n != "x":
                    s += n
        return s * called_number


def start_bingo(p_data):
    numbers, boards = p_data
    scores = []
    for n in numbers:
        for m in boards:
            if m.bingo:
                continue
            m.mark_number(n)
            if m.bingo:
                scores.append(m.count_board(n))
    return scores


def parse_input(data):
    numbers = [int(n) for n in data[0].split(",")]
    boards = []
    for line in data[1:]:
        if not line:
            boards.append(BingoBoard())
            continue
        row = [int(n) for n in line.split()]
        boards[-1].add_row(row)
    return (numbers, boards)


if __name__ == "__main__":
    data = read_file("input.txt")
    p_data = parse_input(data)
    scores = start_bingo(p_data)
    print("Part1: ", scores[0])
    print("Part2: ", scores[-1])
