from template import Template


def score(hand):
    counts = [hand.count(x) for x in hand]
    print(6, counts)
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


def replacemnts(hand):
    if hand == "":
        return [""]

    stack = [("", hand)]
    result = []

    while stack:
        prefix, remaining = stack.pop()
        if remaining == "":
            result.append(prefix)
        else:
            for char in ("23456789TQKA" if remaining[0] == "J" else remaining[0]):
                stack.append((prefix + char, remaining[1:]))

    return result


def classify(hand):
    return max(map(score, replacemnts(hand)))


def strength_1(hand):
    letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
    print(46, hand)
    print(47, score(hand))
    print(48, [letter_map.get(x, x) for x in hand])
    return (score(hand), [letter_map.get(x, x) for x in hand])


def strength_2(hand):
    letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}
    return (classify(hand), [letter_map.get(x, x) for x in hand])


plays = []


class day0(Template):
    def __init__(self):
        self.day = 7
        super().__init__(self.day, file_location="test.txt")
        self.set_data(self.get_data().split("\n"))

        # super().__init__(self.day)
        # self.set_data(self.get_data().split("\n")[:-1])

        for line in self.get_data():
            hand, bid = line.split()
            plays.append((hand, int(bid)))

    def part1(self):
        plays.sort(key=lambda play: strength_1(play[0]))
        total = 0
        for rank, play in enumerate(plays):
            total += play[1] * (rank + 1)
        return total

    def part2(self):
        plays.sort(key=lambda play: strength_2(play[0]))
        total = 0
        for rank, play in enumerate(plays):
            total += play[1] * (rank + 1)
        return total


print(day0())
