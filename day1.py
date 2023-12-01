from template import Template


class day1(Template):
    def __init__(self):
        self.day = 1
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n"))

    def part1(self):
        print(self.get_data())

    def part2(self):
        pass


print(day1())