import numpy as np

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
    s = 0
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
                s += (1 + int(grid[x][y].strip()))
    print(s)

def look_around(file):
    grid = initialize_grid(file)
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if int(grid[x][y].strip()) < 9 and int(grid[x][y].strip() != 'x'):
                print(basincheck(grid, x, y))

def basincheck(grid, x, y):
    surr = 0
    grid[x][y] = 'x'
    if int(grid[x][y] < 0):
        return true
    elif int(grid[x][y].strip() < 9):
        surr+=1
    return surr


def main():
    sum_lows("aoc_day9.txt")
    look_around("aoc_day9.txt")


if __name__ == '__main__':
    main()




























# import sys
# import re
# from collections import defaultdict
#
# def part1(file):
#     counter = 0
#     linec = 0
#     for line in file:
#         for i in line:
#             if linec == 0:
#                 if i - 1 > i and i + 1 > i and line[i + 1][i] > i:
#                     counter += 1
#             elif linec == 100:
#                 if i - 1 > i and i + 1 > i and line[i - 1][i] > i:
#                     counter += 1
#             else:
#                 if i - 1 > i and i + 1 > i and line[i - 1][i] > i and line[i + 1][i] > i:
#                     counter += 1
#             linec+=1
#     print(counter)
#
#
# if __name__ == '__main__':
#     f = open("aoc_day9.txt")
#     part1(f)
