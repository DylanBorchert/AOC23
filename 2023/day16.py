from template import Template
from collections import deque


class day0(Template):
    def __init__(self):
        self.day = 16
        self.year = 2023
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        grid = self.get_data()
        # r, c, dr, dc
        a = [(0, -1, 0, 1)]
        seen = set()
        q = deque(a)

        while q:
            r, c, dr, dc = q.popleft()

            r += dr
            c += dc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            ch = grid[r][c]

            if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "/":
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            elif ch == "\\":
                dr, dc = dc, dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
            else:
                for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                    if (r, c, dr, dc) not in seen:
                        seen.add((r, c, dr, dc))
                        q.append((r, c, dr, dc))

        coords = {(r, c) for r, c, _, _ in seen}

        return len(coords)

    def part2(self):
        return None


print(day0().submit())
