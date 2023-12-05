import math
from template import Template


def group_numbers(array):
    new_array = []
    i = 0
    while i < len(array):
        if array[i].isdigit():
            # Combine consecutive digits
            number = array[i]
            i += 1
            while i < len(array) and array[i].isdigit():
                number += array[i]
                i += 1
            # Append the number three times
            new_array.extend([number] * len(str(number)))
        else:
            new_array.append(array[i])
            i += 1
    return new_array


class day0(Template):
    def __init__(self):
        self.day = 3
        super().__init__(self.day)

        self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        data = [group_numbers(x) for x in self.get_data()]
        sum = 0
        for row, line in enumerate(data):
            for col, char in enumerate(line):
                if not char.isdigit() and char != ".":
                    saved_number = 0
                    for i in range(max(0, row - 1), min(row + 2, len(data))):
                        for j in range(max(0, col - 1), min(col + 2, len(data[i]))):
                            if not data[i][j].isdigit():
                                saved_number = 0
                            if data[i][j].isdigit() and int(data[i][j]) != saved_number:
                                saved_number = int(data[i][j])
                                sum += int(data[i][j])
        return sum

    def part2(self):
        data = [group_numbers(x) for x in self.get_data()]
        sum = 0
        for row, line in enumerate(data):
            for col, char in enumerate(line):
                if char == "*":
                    saved_number = 0
                    all_nums = []
                    for i in range(max(0, row - 1), min(row + 2, len(data))):
                        for j in range(max(0, col - 1), min(col + 2, len(data[i]))):
                            if not data[i][j].isdigit():
                                saved_number = 0
                            if data[i][j].isdigit() and int(data[i][j]) != saved_number:
                                saved_number = int(data[i][j])
                                all_nums.append(int(data[i][j]))
                    if len(all_nums) == 2:
                        sum += math.prod(all_nums)
        return sum


print(day0())
