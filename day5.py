from template import Template


class day0(Template):
    def __init__(self):
        self.day = 5
        # super().__init__(self.day, file_location="test.txt")
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n\n"))

    def part1(self):
        seeds, *blocks = self.get_data()
        # separate the seeds from the ranges
        seeds = [int(x) for x in seeds.split(":")[1].split()]
        for block in blocks:  # iterate through each block
            ranges = []
            # iterate through each line in the block excluding titile and add to list of ranges for each block
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            new = []
            # now go through each sees and check if it is in a range
            for x in seeds:
                for a, b, c in ranges:
                    # convert from source range to target range
                    # if seed fits in source range, add to seed map
                    if x in range(b, b + c):
                        new.append(x - b + a)
                        break
                else:
                    new.append(x)
            seeds = new  # new seed map to g through rest of map
        return min(seeds)

    def part2(self):
        inputs, *blocks = self.get_data()
        inputs = [int(x) for x in inputs.split(":")[1].split()]
        seeds = []
        for i in range(0, len(inputs), 2):
            seeds.append((inputs[i], inputs[i] + inputs[i+1]))

        for block in blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            new = []
            while seeds:
                s, e = seeds.pop()
                for a, b, c in ranges:
                    overlap_start = max(s, b)
                    overlap_end = min(e, b + c)
                    if overlap_start < overlap_end:
                        new.append(
                            (overlap_start - b + a, overlap_end - b + a))
                        if overlap_start > s:
                            seeds.append((s, overlap_start))
                        if overlap_end < e:
                            seeds.append((overlap_end, e))
                        break
                else:
                    new.append((s, e))
            seeds = new
        return min(seeds)[0]


print(day0())
