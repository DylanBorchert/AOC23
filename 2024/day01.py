from template import Template


class day0(Template):
    def __init__(self):
        self.day = 1
        self.year = 2024
        super().__init__(self.day, self.year)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        res = [x.split('   ') for x in self.get_data()]
        left = sorted([int(item[0]) for item in res])
        right = sorted([int(item[1]) for item in res])

        sum = 0
        for i in range(len(left)):
            sum += abs(left[i] + right[i])
        return sum

    def part2(self):
        res = [x.split('   ') for x in self.get_data()]
        left = sorted([int(item[0]) for item in res])
        right = sorted([int(item[1]) for item in res])

        sum = 0
        for i in range(len(left)):
            sum += right.count(left[i]) * left[i]
        return sum


print(day0())
