from template import Template
import re
from statistics import mean


class day0(Template):
    grid = []

    def cycle(self):
        print("Before:")
        print('\n'.join(self.grid))
        self.grid = [''.join(x)for x in list(zip(*self.grid))[::-1]]
        for i, row in enumerate(self.grid):
            total_matches = len(re.findall(r'O\.', row))
            while total_matches > 0:
                row = re.sub(r'O\.', '.O', row)
                total_matches = len(re.findall(r'O\.', row))
            self.grid[i] = row
        print("After:")
        print('\n'.join(self.grid))

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
        seen = [self.get_data()]
        self.grid = self.get_data()
        iterations = 0
        while True:
            iterations += 1
            print(f'After {iterations} cycles:')
            self.cycle()
            if self.grid in seen:
                print(f'Found a cycle at {iterations}')
                break
            seen.append(self.grid)

        first = seen.index(self.grid)
        print(f'First occurrence at {first}')
        self.grid = seen[(1000000000 - first) % (iterations - first) + first]

        [print(row) for row in self.grid]
        return sum(row.count("O") * (len(self.grid) - r) for r, row in enumerate(self.grid))


print(day0())
