from template import Template
from itertools import combinations


class day0(Template):
    def __init__(self):
        self.day = 12
        super().__init__(self.day, useFile=True)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        for i, springs in enumerate(self.get_data()):
            spring, condition = springs.split(" ")
            condition = [int(x) for x in condition.split(",")]
            unkowns = spring.count("?")
            broken = spring.count("#")
            opperational = len(spring) - broken

            unknown_indexs = []
            for i, ch in enumerate(spring):
                if ch == "?":
                    unknown_indexs.append(i)

    def part2(self):
        pass


print(day0())
