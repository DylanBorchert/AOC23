from template import Template


def isSafe(row):
    diffList = []
    for idx in range(len(row)-1):
        diffList.append(row[idx] - row[idx+1])
    if all(0 < num < 4 for num in diffList) or all(-4 < num < 0 for num in diffList):
        return True
    return False


class day0(Template):
    def __init__(self):
        self.day = 2
        self.year = 2024
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        data = [[int(item) for item in x.split(" ")] for x in self.get_data()]
        count = 0
        for row in data:
            diffList = []
            for idx in range(len(row)-1):
                diffList.append(row[idx] - row[idx+1])
            if all(0 < num < 4 for num in diffList) or all(-4 < num < 0 for num in diffList):
                count += 1
        return count

    def part2(self):
        data = [[int(item) for item in x.split(" ")] for x in self.get_data()]
        count = 0
        for row in data:
            if isSafe(row):
                count += 1
            else:
                for i in range(len(row)):
                    modified_row = row[:i] + row[i + 1:]
                    if isSafe(modified_row):
                        count += 1
                        break

        return count


print(day0())
