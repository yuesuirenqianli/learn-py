"""4.10.2"""

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


if __name__ == '__main__':
    for row in range(len(grid[0])):
        print()
        for col in range(len(grid)):
            if grid[col][row]:
                print(grid[col][row], end='')
