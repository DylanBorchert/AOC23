from template import Template
from collections import deque


class day0(Template):
    def __init__(self):
        self.day = 10
        super().__init__(self.day, useFile=True)
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
        seen = {(sr, sc)}
        q = deque([(sr, sc)])

        s_possibilities = {"|", "-", "7", "J", "L", "F"}

        while q:
            r, c = q.popleft()
            ch = grid[r][c]
            # up and can go up and not seen
            if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r-1, c) not in seen:
                seen.add((r-1, c))
                q.append((r-1, c))
                if ch == "S":
                    s_possibilities &= {"|", "J", "F"}
            # down and can go down and not seen
            if r < len(grid)-1 and ch in "S|7F" and grid[r+1][c] in "|JL" and (r+1, c) not in seen:
                seen.add((r+1, c))
                q.append((r+1, c))
                if ch == "S":
                    s_possibilities &= {"|", "7", "F"}
            # left and can go left and not seen
            if c > 0 and ch in "S-J7" and grid[r][c-1] in "-LF" and (r, c-1) not in seen:
                seen.add((r, c-1))
                q.append((r, c-1))
                if ch == "S":
                    s_possibilities &= {"-", "J", "7"}
            # right and can go right and not seen
            if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c+1] in "-J7" and (r, c+1) not in seen:
                seen.add((r, c+1))
                q.append((r, c+1))
                if ch == "S":
                    s_possibilities &= {"-", "L", "F"}

        start_pipe = s_possibilities.pop()

        grid = [row.replace("S", start_pipe) for row in grid]

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                print(grid[r][c], end="")
            print()


print(day0())
