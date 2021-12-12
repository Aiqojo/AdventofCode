import sys
import re

basin = []

def initialize_grid(filename):
    f = open(filename, 'r')
    grid = []
    for line in f:
        s = line.strip()
        row = [ch for ch in s]
        grid.append(row)
    return grid


def sum_lows(filename):
    grid = initialize_grid(filename)
    basin_sizes = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            lowest = True
            if x > 0:
                if int(grid[x][y].strip()) >= int(grid[x - 1][y].strip()):
                    lowest = False
            if y > 0:
                if int(grid[x][y].strip()) >= int(grid[x][y - 1].strip()):
                    lowest = False
            if x < len(grid) - 1:
                if int(grid[x][y].strip()) >= int(grid[x + 1][y].strip()):
                    lowest = False
            if y < len(grid[0]) - 1:
                if int(grid[x][y].strip()) >= int(grid[x][y + 1].strip()):
                    lowest = False
            if lowest:
                basin.clear()
                find_basin_size((x, y), grid)
                basin_sizes.append(len(basin))
    size = sorted(basin_sizes)
    res = size[-1] * size[-2] * size[-3]
    print(res)


def find_basin_size(coords, grid):
    x = coords[0]
    y = coords[1]
    basin.append((x, y))
    if x > 0 and (not (x - 1, y) in basin):
        # check
        if int(grid[x][y].strip()) < int(grid[x - 1][y]) and int(grid[x - 1][y]) != 9:
            find_basin_size((x - 1, y), grid)
    if y > 0 and (not (x, y - 1) in basin):
        # check
        if int(grid[x][y].strip()) < int(grid[x][y - 1]) and int(grid[x][y - 1]) != 9:
            find_basin_size((x, y - 1), grid)
    if x < len(grid) - 1 and (not (x + 1, y) in basin):
        # check
        if int(grid[x][y].strip()) < int(grid[x + 1][y]) and int(grid[x + 1][y]) != 9:
            find_basin_size((x + 1, y), grid)
    if y < len(grid[0]) - 1 and (not (x, y + 1) in basin):
        # check
        if int(grid[x][y].strip()) < int(grid[x][y + 1]) and int(grid[x][y + 1]) != 9:
            find_basin_size((x, y + 1), grid)


def main():
    sum_lows("aoc_day9.txt")
    # look_around("aoc_day9.txt")


if __name__ == '__main__':
    main()
