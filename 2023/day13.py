from template import Template


def find_mirrow_part1(block):
    for row in range(1, len(block)):
        above = block[:row][::-1]
        below = block[row:]

        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return row
    return 0


def find_mirrow_part2(block):
    for row in range(1, len(block)):
        above = block[:row][::-1]
        below = block[row:]
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return row
    return 0


class day0(Template):
    def __init__(self):
        self.day = 13
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n\n"))

    def part1(self):
        data = [x.split("\n") for x in self.get_data()]
        total = 0
        for block in data:
            row = find_mirrow_part1(block)
            total += row * 100
            row = find_mirrow_part1(list(zip(*block)))
            total += row
        return total

    def part2(self):
        data = [x.split("\n") for x in self.get_data()]
        total = 0
        for block in data:
            row = find_mirrow_part2(block)
            total += row * 100
            row = find_mirrow_part2(list(zip(*block)))
            total += row
        return total


print(day0())
