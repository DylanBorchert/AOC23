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
        times, distances = [list(map(int, x.split(":")[1].split()))
                            for x in self.get_data()]
        product = 1
        for time, distance in zip(times, distances):
            ways = 0
            for hold_time in range(time):
                if hold_time * (time - hold_time) > distance:
                    ways += 1
            product *= ways
        return product

    def part2(self):
        time, distance = [int(x.split(":")[1].replace(" ", ""))
                          for x in self.get_data()]
        product = 1
        ways = 0
        for hold_time in range(time):
            if hold_time * (time - hold_time) > distance:
                ways += 1
        product *= ways
        return product


print(day0())
