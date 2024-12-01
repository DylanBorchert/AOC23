from template import Template


class day0(Template):
    def __init__(self):
        self.day = 0
        self.year = 2024
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        return None

    def part2(self):
        return None


print(day0())
