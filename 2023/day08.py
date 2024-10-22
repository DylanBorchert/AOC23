from math import gcd
import math
from template import Template

import sys
sys.setrecursionlimit(100000)


class day0(Template):
    instructions = []
    network = {}

    def __init__(self):
        self.day = 8
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().split("\n\n"))

        self.instructions = self.get_data()[0].strip()

        for i, n in enumerate(self.get_data()[1].split("\n")[:-1]):
            net, target = n.split(" = ")
            self.network[net] = target[1:-1].split(", ")

    def part1(self):
        current_steps = self.instructions
        tag = "AAA"
        steps_count = 0
        while tag != "ZZZ":
            tag = self.network[tag][0 if current_steps[0] == "L" else 1]
            current_steps = current_steps[1:] + current_steps[0]
            steps_count += 1
        return steps_count

    def part2(self):
        posistions = [x for x in self.network if x.endswith("A")]

        cycles = []

        for current in posistions:
            cycle = []

            current_steps = self.instructions
            step_count = 0
            first_z = None

            while True:
                while step_count == 0 or not current.endswith("Z"):
                    step_count += 1
                    current = self.network[current][0 if current_steps[0]
                                                    == "L" else 1]
                    current_steps = current_steps[1:] + current_steps[0]

                cycle.append(step_count)

                if first_z is None:
                    first_z = current
                    step_count = 0
                elif current == first_z:
                    print(cycle)
                    break

            cycles.append(cycle)

        nums = [cycle[0] for cycle in cycles]

        return math.lcm(*nums)


print(day0())
