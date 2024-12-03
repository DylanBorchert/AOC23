import re
from template import Template


class day0(Template):
    def __init__(self):
        self.day = 3
        self.year = 2024
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip())

    def part1(self):
        regex_mul = r"mul\((\d+),(\d+)\)"
        matches = re.findall(regex_mul, self.get_data())
        data = [[int(num1), int(num2)] for num1, num2 in matches]

        product = 0
        for numbers in data:
            product += numbers[0] * numbers[1]
        return product

    def part2(self):
        regex_mul = r"mul\((\d+),(\d+)\)"
        regex_dont = r"don't\(\)"
        regex_do = r"do\(\)"

        matches = re.finditer(rf"{regex_mul}|{regex_dont}|{regex_do}", self.get_data())

        product = 0
        allow_mul = True

        for match in matches:
            if match.group(1):  # Matches "mul(x, y)"
                if allow_mul:
                    product += int(match.group(1)) * int(match.group(2))
            elif "don't()" in match.group(0):  # Matches "don't()"
                allow_mul = False
            elif "do()" in match.group(0):  # Matches "do()"
                allow_mul = True

        return product


print(day0())
