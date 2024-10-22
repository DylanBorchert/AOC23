from template import Template


class day0(Template):
    def __init__(self):
        self.day = 0
        self.year = 2024
        super().__init__(self.day, self.year, useFile=True)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        return 0

    def part2(self):
        return 0


print(day0().submit())
