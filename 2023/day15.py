from template import Template


def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v


class day0(Template):
    def __init__(self):
        self.day = 15
        self.year = 2023
        super().__init__(self.day, self.year, useFile=True)
        self.set_data(self.get_data().strip().split(","))

    def part1(self):
        sequence = self.get_data()
        return sum([hash(s) for s in sequence])

    def part2(self):
        boxes = [[] for _ in range(256)]
        focal_lengths = {}
        for instructions in self.get_data():
            if "-" in instructions:
                label = instructions[:-1]
                index = hash(label)
                if label in boxes[index]:
                    boxes[index].remove(label)
            else:
                label, length = instructions.split("=")
                length = int(length)

                index = hash(label)
                if label not in boxes[index]:
                    boxes[index].append(label)

                focal_lengths[label] = length

        total = 0
        for box_number, box in enumerate(boxes, 1):
            for lens_slot, label in enumerate(box, 1):
                total += box_number * lens_slot * focal_lengths[label]

        return total


print(day0().submit())
