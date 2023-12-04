from template import Template


class day0(Template):
    def __init__(self):
        self.day = 4
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        return self.get_data()

    def part2(self):
        pass


print(day0())
