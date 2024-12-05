from template import Template


class day0(Template):
    def __init__(self):
        self.day = 4
        self.year = 2024
        super().__init__(self.day, self.year, useFile=False)
        self.set_data(self.get_data().strip().split("\n"))

    def part1(self):
        grid = self.get_data()
        xmas = ['XMAS', 'SAMX']

        count = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in grid:
            count += sum(row.count(s) for s in xmas)

        for col in range(cols):
            column = ''.join(grid[row][col] for row in range(rows))
            count += sum(column.count(s) for s in xmas)

        # Diagonal top-left to bottom-right
        for d in range(-(rows - 1), cols):
            diagonal = ''.join(
                grid[r][c] for r in range(rows) for c in range(cols) if r - c == d
            )
            count += sum(diagonal.count(s) for s in xmas)

        # Diagonal top-right to bottom-left
        for d in range(rows + cols - 1):
            diagonal = ''.join(
                grid[r][c] for r in range(rows) for c in range(cols) if r + c == d
            )
            count += sum(diagonal.count(s) for s in xmas)

        return count

    def part2(self):
        grid = self.get_data()

        count = 0

        rows = len(grid)
        cols = len(grid[0])

        valid_mas = ['SAM', 'MAS']

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 'A':
                    tl_br = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
                    tr_bl = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
                    if (tl_br in valid_mas and tr_bl in valid_mas):
                        count += 1

        return count


print(day0())
