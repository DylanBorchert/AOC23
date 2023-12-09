from template import Template


class day0(Template):
    def __init__(self):
        self.day = 9
        super().__init__(self.day)
        self.set_data([list(map(int, x.split()))
                      for x in self.get_data().strip().split("\n")])

        # super().__init__(self.day)
        # self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        total = 0
        for i, row in enumerate(self.get_data()):
            triangle = [row]
            current_row = row

            while len(current_row) > 1:
                # Subtract adjacent elements

                current_row = [current_row[i + 1] - current_row[i]
                               for i in range(len(current_row) - 1)]
                triangle.append(current_row)
                if len([x for x in current_row if x == 0]) == len(current_row):
                    break
            total += sum([x[-1] for x in triangle])

        return total

    def part2(self):
        total = 0
        for i, row in enumerate(self.get_data()):
            triangle = [row]
            current_row = row

            while len(current_row) > 1:
                # Subtract adjacent elements

                current_row = [current_row[i + 1] - current_row[i]
                               for i in range(len(current_row) - 1)]
                triangle.append(current_row)
                if len([x for x in current_row if x == 0]) == len(current_row):
                    break

            line_total = 0
            for line in triangle[::-1][1:]:
                line_total = line[0] - line_total

            total += line_total

        return total


print(day0())
