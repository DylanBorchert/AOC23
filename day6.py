import math

import numpy
from template import Template


class day0(Template):
    def __init__(self):
        self.day = 6
        # super().__init__(self.day, file_location="test.txt")
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        times = [int(x) for x in self.get_data()[0].split(":")[1].split()]
        distances = [int(x) for x in self.get_data()[1].split(":")[1].split()]
        product = 1
        for i, time in enumerate(times):
            ways = 0
            for hold_time in range(time):
                total_distance = hold_time * (time - hold_time)
                if total_distance > distances[i]:
                    ways += 1
            product *= ways
        return product

    def part2(self):
        time = int(self.get_data()[0].split(":")[1].replace(" ", ""))
        distance = int(self.get_data()[1].split(":")[1].replace(" ", ""))
        product = 1
        ways = 0
        for hold_time in range(time):
            total_distance = hold_time * (time - hold_time)
            if total_distance > distance:
                ways += 1
        product *= ways
        return product


print(day0())
