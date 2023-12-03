from template import Template


class day2(Template):
    def __init__(self):
        self.day = 2
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        possible = 0
        data = [x.strip().split(": ")[1].split("; ") for x in self.get_data()]

        for i, x in enumerate(data):
            for y in x:
                colors = {"red": 0, "green": 0, "blue": 0}
                y = y.split(", ")
                for z in y:  # go through each turn check if the limit is broken
                    n, c = z.split(" ")  # get the color and number
                    # at any point if the color is greater than the limit, break
                    colors[c] = int(n)
                if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                    break
            else:
                possible += i + 1
        return possible

    def part2(self):
        possible = 0
        data = [x.strip().split(": ")[1].split("; ") for x in self.get_data()]

        for i, x in enumerate(data):
            # look at each turn and find the max color
            max_color = {"red": 0, "green": 0, "blue": 0}
            for y in x:  # go through each turn check to get colors and find new max
                colors = {"red": 0, "green": 0, "blue": 0}
                y = y.split(", ")
                for z in y:
                    n, c = z.split(" ")  # get the color and number
                    colors[c] = int(n)
                for c in colors:  # find the max color
                    max_color[c] = max(max_color[c], colors[c])
            else:
                possible += max_color["red"] * \
                    max_color["green"] * \
                    max_color["blue"]  # multiply the max colors
        return possible


print(day2())
