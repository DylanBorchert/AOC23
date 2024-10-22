from template import Template
import numpy as np

cache = {}


def count(springs, groups):
    if springs == "":
        return 1 if groups == () else 0

    if groups == ():
        return 0 if "#" in springs else 1

    key = (springs, groups)

    if key in cache:
        return cache[key]

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], groups)

    if springs[0] in "#?":
        if groups[0] <= len(springs) and "." not in springs[:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != "#"):
            result += count(springs[groups[0] + 1:], groups[1:])

    cache[key] = result
    return result


class day0(Template):
    def __init__(self):
        self.day = 12
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        total = 0
        for i, springs in enumerate(self.get_data()):
            springs, groups = springs.split(" ")
            groups = tuple(map(int, groups.split(",")))

            total += count(springs, groups)
        return total

    def part2(self):
        total = 0
        for i, springs in enumerate(self.get_data()):
            springs, groups = springs.split(" ")
            groups = tuple(map(int, groups.split(",")))

            groups = (groups * 5)

            new_springs = ""
            for i in range(5):
                new_springs = new_springs + springs + "?"
            springs = new_springs[:-1]

            total += count(springs, groups)
        return total


print(day0())
