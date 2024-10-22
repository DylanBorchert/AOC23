from functools import reduce
import re

from template import Template

text_to_digit = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]


def extract_digits(line):
    for text, digit in text_to_digit.items():
        line = re.sub(r'\b' + text + r'\b', digit, line)
    return line


class day1(Template):
    def __init__(self):
        self.day = 1
        self.year = 2023
        super().__init__(self.day, self.year)

        self.set_data(self.get_data().split("\n")[:-1])

    def part1(self):
        # sum of the first and last digits of each line
        return sum([int(t[0] + t[-1]) for t in [re.sub("[^0-9]", "", x) for x in self.get_data()]])

    def part2(self):
        sum = 0
        for line in self.get_data():
            digits = []  # list of digits in the line
            # iterate through each character in the line
            for i, char in enumerate(line):
                if char.isdigit():  # if the character is a digit, add it to the list
                    digits.append(char)
                # loops through array of text representations of digits
                for d, val in enumerate(text_to_digit):
                    # looks ahead for the text representation of a digit and if foud, adds the digit to the list
                    if line[i:].startswith(val):
                        digits.append(str(d+1))
            # calculates the score for the line
            score = int(digits[0] + digits[-1])
            sum += score  # adds the score to the total sum
        return sum


day1().submit()
