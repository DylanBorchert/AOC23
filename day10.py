from template import Template
from collections import deque


class day0(Template):
    def __init__(self):
        self.day = 10
        super().__init__(self.day, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        grid = self.get_data()
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "S":
                    sr, sc = r, c
                    break
            else:
                continue
            break
        seen = {(sr, sc)}
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            ch = grid[r][c]
            # up and can go up and not seen
            if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r-1, c) not in seen:
                seen.add((r-1, c))
                q.append((r-1, c))
            # down and can go down and not seen
            if r < len(grid)-1 and ch in "S|7F" and grid[r+1][c] in "|JL" and (r+1, c) not in seen:
                seen.add((r+1, c))
                q.append((r+1, c))
            # left and can go left and not seen
            if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r, c-1) not in seen:
                seen.add((r, c-1))
                q.append((r, c-1))
            # right and can go right and not seen
            if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in seen:
                seen.add((r, c+1))
                q.append((r, c+1))

        return len(seen)//2

    def part2(self):
        grid = self.get_data()
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "S":
                    sr, sc = r, c
                    break
            else:
                continue
            break
        loop = {(sr, sc)}
        q = deque([(sr, sc)])

        s_possibilities = {"|", "-", "7", "J", "L", "F"}

        while q:
            r, c = q.popleft()
            ch = grid[r][c]
            # up and can go up and not seen
            if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r-1, c) not in loop:
                loop.add((r-1, c))
                q.append((r-1, c))
                if ch == "S":
                    s_possibilities &= {"|", "J", "F"}
            # down and can go down and not seen
            if r < len(grid)-1 and ch in "S|7F" and grid[r+1][c] in "|JL" and (r+1, c) not in loop:
                loop.add((r+1, c))
                q.append((r+1, c))
                if ch == "S":
                    s_possibilities &= {"|", "7", "F"}
            # left and can go left and not seen
            if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r, c-1) not in loop:
                loop.add((r, c-1))
                q.append((r, c-1))
                if ch == "S":
                    s_possibilities &= {"-", "J", "7"}
            # right and can go right and not seen
            if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in loop:
                loop.add((r, c+1))
                q.append((r, c+1))
                if ch == "S":
                    s_possibilities &= {"-", "L", "F"}

        start_pipe = s_possibilities.pop()

        grid = [row.replace("S", start_pipe) for row in grid]
        grid = ["".join(ch if (r, c) in loop else "." for c,
                        ch in enumerate(row)) for r, row in enumerate(grid)]

        outside = set()

        for r, row in enumerate(grid):
            within = False
            up = None
            for c, ch in enumerate(row):
                if ch == "|":
                    within = not within
                elif ch in "LF":  # start of pipe riding
                    up = ch == "L"
                elif ch == "-":  # riding pipe
                    pass
                elif ch in "7J":  # check for riding along pipe or crossing pipe
                    if ch != ("J" if up else "7"):
                        within = not within
                    up = None
                elif ch == ".":  # emply space
                    pass
                if not within:
                    outside.add((r, c))

        return len(grid) * len(grid[0]) - len(outside | loop)


print(day0())
