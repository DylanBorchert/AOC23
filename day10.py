from template import Template


class day0(Template):
    def __init__(self):
        self.day = 10
        super().__init__(self.day, useFile=True)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        return self.get_data()

    def part2(self):
        pass


print(day0())
