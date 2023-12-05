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
                        # seed location minus source range start plus target range start
                        new.append(x - b + a)
                        break
                else:
                    # if seed does not fit in source range, add to seed map
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
            # keep going through seeds until there are no more seeds
            while seeds:
                s, e = seeds.pop()
                for a, b, c in ranges:
                    #  seed     |---Seed range---|
                    #       |---s----------------e------|
                    #       b---------------------------b+c
                    overlap_start = max(s, b)  # find the start overlap
                    overlap_end = min(e, b + c)  # find the end overlap
                    if overlap_start < overlap_end:  # if there is an overlap
                        new.append(
                            (overlap_start - b + a, overlap_end - b + a))  # add the new seed
                        if overlap_start > s:  # if there is a seed before the overlap
                            seeds.append((s, overlap_start))
                        if overlap_end < e:  # if there is a seed after the overlap
                            seeds.append((overlap_end, e))
                        break
                else:
                    # if there is no overlap, add the seed back
                    new.append((s, e))
            seeds = new
        return min(seeds)[0]


print(day0())
