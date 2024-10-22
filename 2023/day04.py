from template import Template
import numpy as np


class day0(Template):
    def __init__(self):
        self.day = 4
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)

        self.set_data([x.split(":")[1]
                      for x in self.get_data().split("\n")[:-1]])

    def part1(self):
        sum = 0
        for i, line in enumerate(self.get_data()):
            wins = 0
            winning_nums = [int(x) for x in line.split(
                "|")[0].strip().replace("  ", " ").split(" ")]
            your_nums = [int(x) for x in line.split(
                "|")[1].strip().replace("  ", " ").split(" ")]
            for num in winning_nums:
                if num in your_nums:
                    wins += 1
            sum += int(pow(2, wins - 1))
        return sum

    def part2(self):
        points = [x for x in np.ones(len(self.get_data()), dtype=int)]
        for i, line in enumerate(self.get_data()):
            wins = 0
            winning_nums = [int(x) for x in line.split(
                "|")[0].strip().replace("  ", " ").split(" ")]
            your_nums = [int(x) for x in line.split(
                "|")[1].strip().replace("  ", " ").split(" ")]
            for num in winning_nums:
                if num in your_nums:
                    wins += 1
            for j in range(wins):
                hole = i + j + 1
                points[hole] = points[hole] + points[i]
        return sum(points)


print(day0())
