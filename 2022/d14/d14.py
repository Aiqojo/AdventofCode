import numpy as np
import matplotlib.image

inp = []
for line in open("t14.txt", "r"):
    inp.append(line.strip())


def parse(inp):
    ret = []
    for line in inp:
        ii = []
        ins = line.split(" -> ")
        for i in ins:
            iii = i.split(",")
            iii = [int(x) for x in iii]
            ii.append(iii)
        ret.append(ii)
    return ret


inst = parse(inp)


def make_cave(inp):
    # find the lowest x so we can normalize it as 0
    min_x = min([min([x[0] for x in i]) for i in inp])
    max_x = max([max([x[0] for x in i]) for i in inp])
    min_y = 0
    max_y = max([max([x[1] for x in i]) for i in inp])
    cave = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=np.int32)

    # for each input
    for i in inp:
        for j in range(1, len(i)):
            # find origin x and y
            (ox, oy) = i[j - 1][0] - min_x, i[j - 1][1] - min_y
            # find end point x and y
            (ex, ey) = i[j][0] - min_x, i[j][1] - min_y
            # get all values between origin and end point
            # print(ox, oy, ex, ey)
            if ox == ex:
                if oy > ey:
                    cave[ey : oy + 1, ox] = 1
                else:
                    cave[oy : ey + 1, ox] = 1
            else:
                if ox > ex:
                    cave[oy, ex : ox + 1] = 1
                else:
                    cave[oy, ox : ex + 1] = 1

    cave[0, 500 - min_x] = 2

    return cave, min_x


grid, min_x = make_cave(inst)
print(grid)

# part 2
# add empty space to left and right
grid = np.pad(grid, ((0, 0), (200, 200)), "constant", constant_values=0)

# add two rows to the bottom, the first row is all 0s, the second row is all 1s
grid = np.vstack((grid, np.zeros((1, grid.shape[1]), dtype=np.int32)))
grid = np.vstack((grid, np.ones((1, grid.shape[1]), dtype=np.int32)))


def check_bounds(grid, x, y):
    if x < 0 or x >= grid.shape[1]:
        return False
    if y < 0 or y >= grid.shape[0]:
        return False
    return True


def place(grid, sand_x, sand_y):
    while True:
        moved = False
        # check if we can move down
        if grid[sand_y + 1, sand_x] == 0:
            grid[sand_y, sand_x] = 0 if grid[sand_y, sand_x] != 2 else 2
            sand_y += 1
            val = check_bounds(grid, sand_x, sand_y)
            if val == False:
                break
            moved = True
            grid[sand_y, sand_x] = 3
            continue
        else:
            # check if we can fill down and to left
            if grid[sand_y + 1, sand_x - 1] == 0:
                grid[sand_y, sand_x] = 0 if grid[sand_y, sand_x] != 2 else 2
                sand_x -= 1
                sand_y += 1
                val = check_bounds(grid, sand_x, sand_y)
                if val == False:
                    break
                moved = True
                grid[sand_y, sand_x] = 3
                continue
            # check if we can fill down and to right
            if grid[sand_y + 1, sand_x + 1] == 0:
                grid[sand_y, sand_x] = 0 if grid[sand_y, sand_x] != 2 else 2
                sand_x += 1
                sand_y += 1
                val = check_bounds(grid, sand_x, sand_y)
                if val == False:
                    break
                moved = True
                grid[sand_y, sand_x] = 3
                continue
        if not moved:
            break

        if grid[sand_x, sand_y] == 2:
            grid[sand_x, sand_y] = 3

    return grid


def fill(grid):
    t_grid = grid.copy()
    count = 0
    while True:
        # matplotlib.image.imsave("cave.png", grid)

        try:
            source = np.where(grid == 2)
        except:
            break
        sand_x = source[1][0]
        sand_y = source[0][0]
        # print(grid)
        try:
            grid = place(grid, sand_x, sand_y)
        except:
            break
        # print(grid)
        if np.array_equal(grid, t_grid):
            break

        count += 1
        print(count)
        t_grid = grid.copy()

    print(count)
    print(grid)
    return grid


grid = fill(grid)
# add 1 for part 2

matplotlib.image.imsave("cave.png", grid)
