from template import Template


def find_mirrow(block):
    for row in range(1, len(block)):
        above = block[:row][::-1]
        below = block[row:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return row
    return 0


class day0(Template):
    def __init__(self):
        self.day = 13
        super().__init__(self.day, useFile=False)
        self.set_data(self.get_data().strip().split("\n\n"))

    def part1(self):
        data = [x.split("\n") for x in self.get_data()]
        total = 0
        for block in data:
            row = find_mirrow(block)
            total += row * 100
            row = find_mirrow(list(zip(*block)))
            total += row
        return total

    def part2(self):
        pass


print(day0())
