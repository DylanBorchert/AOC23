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
        test_data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]
        self.set_data(test_data)

    def part1(self):
        return [group_numbers(list(x)) for x in self.get_data()]

    def part2(self):
        pass


print(day0())
