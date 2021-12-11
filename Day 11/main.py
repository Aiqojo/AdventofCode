# Globals
flashes = 0
rr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
cc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


# Making the grid
def initialize_grid(filename):
    f = open(filename, 'r')
    grid = []
    for line in f:
        s = line.strip()
        row = [int(ch) for ch in s]
        grid.append(row)
    return grid


# part 1 and 2
def part1and2(file):
    # setting stuff up
    global flashes
    step = 0
    counter = 0
    zero = False
    grid = initialize_grid(file)

    while not zero:  # while loop is for part 2
        for r in range(len(grid)):  # over each row
            for c in range(len(grid[0])):  # over each column
                flash(grid, r, c)  # flash each point
        grid = restore(grid)  # restore it, bringing 10s to 0s
        step += 1  # increase step cause one step has gone by
        if step == 100:  # if the step count is 100, enter for part 1
            print(flashes)  # print answer for part 1
        for r in range(len(grid)):  # over each row
            for c in range(len(grid[0])):  # over each column
                counter += int(grid[r][c])  # increase the counter by the amount at each location
        if counter == 0:  # if the counter is 0, that means there is a zero at all locations
            zero = True  # part two is completed
        counter = 0  # this is resetting counter if part two isn't complete
    print(step)  # print answer for part 2


def flash(grid, r, c):  # yummy recursion
    global rr
    global cc
    global flashes
    if not r < 0 and not c < 0 and not r > 9 and not c > 9:  # as long as the location is within bounds
        if grid[r][c] < 9:  # if it is less than 9
            grid[r][c] += 1  # add one and return (base case)
            return grid
        elif grid[r][c] == 9:  # if it is equal to 9
            grid[r][c] += 1  # increase by one
            flashes += 1  # increase flash count by one
            for k in range(9):  # for each other octopus surrounding it, flash them too if they are not equal to 10
                if 0 <= r + rr[k] <= 9 and 0 <= c + cc[k] <= 9 and not grid[r + rr[k]][c + cc[k]] == 10:
                    grid = flash(grid, r + rr[k], c + cc[k])  # flash this location
            return grid  # returning stuff
        return grid
    return grid


def restore(grid):
    for r in range(len(grid)):  # over each row
        for c in range(len(grid[0])):  # over each column
            if grid[r][c] == 10:  # if location is equal to 10
                grid[r][c] = 0  # set to 0
    return grid


def main():
    # part1("test.txt")
    # part1("aoc_day11.txt")
    part1and2("aoc_day11.txt")


if __name__ == '__main__':
    main()

# print("")
#     for q in range(len(map)):
#         print(map[q])
#     global rr
#     global cc
#     global flashes
#     if map[r][c] <= 9 and not map[r][c] < 0:
#         map[r][c] += 1
#         map[r][c] *= -1
#         map = flash(map, r, c)
#         # map = aoe(map, r, c)
#         return map
#     elif map[r][c] > 9:
#         map[r][c] = 0
#         flashes += 1
#         for k in rr:
#             for j in cc:
#                 if not r + k < 0 and not c + j < 0 and not r + k > 9 and not c + j > 9:
#                     map = flash(map, r+k, c+j)
#     else:
#         return map
