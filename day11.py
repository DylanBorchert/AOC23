from template import Template
from itertools import combinations


class day0(Template):
    def __init__(self):
        self.day = 11
        super().__init__(self.day, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        empty_space = 2
        data = self.get_data()

        empty_rows = []
        empty_cols = []

        for r, row in enumerate(data):
            if "#" not in row:
                empty_rows.append(r)

        for c, col in enumerate([[*x] for x in list(zip(*data))]):
            if "#" not in col:
                empty_cols.append(c)

        galaxies = set()
        for r, row in enumerate(data):
            for c, col in enumerate(row):
                if col == "#" and (r, c) not in galaxies:
                    galaxies.add((r, c))

        pairs = list(combinations(galaxies, 2))

        total = 0
        for p1, p2 in pairs:
            row_start = min(p1[0], p2[0])
            col_start = min(p1[1], p2[1])
            row_end = max(p1[0], p2[0])
            col_end = max(p1[1], p2[1])
            for i in empty_rows:
                if row_start < i < row_end:
                    total += empty_space - 1
            for i in empty_cols:
                if col_start < i < col_end:
                    total += empty_space - 1
            total += row_end - row_start + col_end - col_start
        return total

    def part2(self):
        empty_space = 1000000
        data = self.get_data()

        empty_rows = []
        empty_cols = []

        for r, row in enumerate(data):
            if "#" not in row:
                empty_rows.append(r)

        for c, col in enumerate([[*x] for x in list(zip(*data))]):
            if "#" not in col:
                empty_cols.append(c)

        galaxies = set()
        for r, row in enumerate(data):
            for c, col in enumerate(row):
                if col == "#" and (r, c) not in galaxies:
                    galaxies.add((r, c))

        pairs = list(combinations(galaxies, 2))

        total = 0
        for p1, p2 in pairs:
            row_start = min(p1[0], p2[0])
            col_start = min(p1[1], p2[1])
            row_end = max(p1[0], p2[0])
            col_end = max(p1[1], p2[1])
            for i in empty_rows:
                if row_start < i < row_end:
                    total += empty_space - 1
            for i in empty_cols:
                if col_start < i < col_end:
                    total += empty_space - 1
            total += row_end - row_start + col_end - col_start
        return total


print(day0())
