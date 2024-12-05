NONE = 0
RIGHT = 1
LEFT = -1
UP = -1
DOWN = 1

def count_direction(grid, row, col, dirRow, dirCol):
    keyword = 'XMAS'
    for c in keyword:
        if row < 0 or row >= rows:
            return 0
        if col < 0 or col >= cols:
            return 0
        if grid[col][row] != c:
            return 0
        row += dirRow
        col += dirCol
    return 1

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[c for c in line.rstrip()] for line in lines]
count = 0
cols = len(grid)
rows = len(grid[0])

for i in range(rows):
    for j in range(cols):
        count += count_direction(grid, i, j, RIGHT, NONE)
        count += count_direction(grid, i, j, LEFT, NONE)
        count += count_direction(grid, i, j, NONE, UP)
        count += count_direction(grid, i, j, NONE, DOWN)
        count += count_direction(grid, i, j, RIGHT, DOWN)
        count += count_direction(grid, i, j, RIGHT, UP)
        count += count_direction(grid, i, j, LEFT, DOWN)
        count += count_direction(grid, i, j, LEFT, UP)

print(count)