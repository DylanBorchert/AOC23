from template import Template
import re
from statistics import mean


class day0(Template):

    def __init__(self):
        self.day = 14
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        self.grid = self.get_data()
        self.grid = [''.join(x)for x in list(zip(*self.grid[::-1]))]
        for i, row in enumerate(self.grid):
            total_matches = len(re.findall(r'O\.', row))
            while total_matches > 0:
                row = re.sub(r'O\.', '.O', row)
                total_matches = len(re.findall(r'O\.', row))
            self.grid[i] = row
        self.grid = [''.join(x)for x in list(zip(*self.grid))[::-1]]
        return sum(row.count("O") * (len(self.grid) - r) for r, row in enumerate(self.grid))

    def part2(self):
        grid = tuple(self.get_data())
        
        states = []
        seen = set()
        index = 0

        while grid not in seen:
            states.append(grid)
            seen.add(grid)
            for _ in range(4):
                grid = list(zip(*grid))
                grid = ["#".join("".join(sorted(block, reverse=True)) for block in "".join(row).split("#")) for row in grid]
                grid = tuple(row[::-1] for row in grid)
            index += 1

        offset = states.index(grid)
        cycle_length = index - offset

        grid = states[(1_000_000_000 - offset) % cycle_length + offset]

        L = len(grid)
        return (sum(row.count("O") * (L - r) for r, row in enumerate(grid)))


print(day0().submit())
