#!/usr/bin/env python

def count_neighbors(grid, row, col):
    count = 0
    neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

    if all(len(grid) == len(grid[i]) for i in range(len(grid))):
        pass
    else:
        print("Not a square")
        raise SystemExit

    if (3 <= len(grid) <= 10):
        pass
    else:
        print("Too big grid")
        raise SystemExit

    for diff in neighbors:
        n_row = row + diff[0]
        n_col = col + diff[1]
        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[n_row]):
            if grid[n_row][n_col]:
                count += 1

    print(count)

#    for i in range(len(grid)):
#        for j in range(len(grid[i])):
#            grid[i][j]
#        print()

count_neighbors(((1, 0, 0, 1, 0),
		 (0, 1, 0, 0, 0),
		 (0, 0, 1, 0, 1),
		 (1, 0, 0, 0, 0),
		 (0, 0, 1, 0, 0),), 1, 2)


