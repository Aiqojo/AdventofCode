import numpy as np
import time


def find_path_lengths(file, part_two):
    grid = np.genfromtxt(file, dtype=int, delimiter=1)
    width = np.shape(grid)[0]
    height = np.shape(grid)[1]
    if part_two:
        new_grid = np.zeros((width * 5, height * 5))
        for i in range(5):
            for j in range(5):
                for x in range(width):
                    for y in range(height):
                        new_val = grid[x, y] + i + j
                        if new_val > 9:
                            new_val -= 9
                        new_grid[i * width + x, j * height + y] = new_val
        grid = new_grid
        width = 5 * width
        height = 5 * height
    dist = np.full((width, height), 999999)
    dist[0, 0] = 0
    vis = set()
    fill_dist(vis, [(0, 0)], grid, dist, (0, 0))
    print(dist[width - 1][height - 1])
    # print(dist)


def fill_dist(curvis, open, grid, dist, loc):
    width = np.shape(grid)[0]
    height = np.shape(grid)[1]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while dist[width - 1, height - 1] == 999999:
        curvis.add(loc)
        open.remove(loc)
        x = loc[0]
        y = loc[1]
        for i in range(4):
            if (0 <= x + dx[i] < width and 0 <= y + dy[i] < height) and not (x + dx[i], y + dy[i]) in curvis:
                if not (x + dx[i], y + dy[i]) in open:
                    open.append((x + dx[i], y + dy[i]))
                dist[x + dx[i], y + dy[i]] = min(dist[x + dx[i], y + dy[i]], dist[x, y] + grid[x + dx[i], y + dy[i]])
        if len(open) == 0:
            return 'cringe'
        low = open[0]
        lowest = dist[open[0][0], open[0][1]]
        for o in open:
            if dist[o[0], o[1]] < lowest:
                lowest = dist[o[0], o[1]]
                low = o
        loc = low


def main():
    start = time.time()
    find_path_lengths("15.txt", False)
    print("Part 1: ", time.time()-start, "sec")
    start = time.time()
    find_path_lengths("15.txt", True)
    print("Part 2: ", time.time() - start, "sec")


if __name__ == '__main__':
    main()
