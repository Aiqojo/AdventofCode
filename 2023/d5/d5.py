import numpy as np
from collections import defaultdict

file = open("d5.txt").read().strip()
with open("d5.txt") as f:
    lines = f.readlines()
    lines = [s.strip() for s in lines]

lines = np.array(lines)
# for line in lines:
#     print(line)
# print(lines.shape)

seeds = [int(c) for c in lines[0].split(":")[1].strip().split()]
print(seeds)

maps = []
for i in range(7):
    maps.append([])

cur_loc = 0
p = 3
# if line ends with semicolon look next line
# if line is empty, increase cur_loc and look next line
# otherwise split the numbers and add to maps
# print()
# print(len(lines))
while cur_loc < len(lines[3:]):
    if lines[p].strip().endswith(":"):
        # print("skip", lines[p])
        p += 1
        continue
    elif lines[p] == "":
        # print("empty", lines[p])
        cur_loc += 1
        p += 1
    else:
        # print("add", lines[p])
        maps[cur_loc].append([int(c) for c in lines[p].strip().split()])
        p += 1

    if p >= len(lines):
        break

# for i in range(len(maps)):
#     print(maps[i])
# print()

final_locs = []
for seed in seeds:
    cur_seed = seed
    # for each conversion
    for i in range(len(maps)):
        # print(cur_seed)
        # looking at each map
        found = False
        for j in range(len(maps[i])):
            # find if seed is in range of map
            # destination, source, range
            # ex: 50, 98, 2: results in [50, 51] [98, 99]
            if cur_seed >= maps[i][j][1] and cur_seed <= maps[i][j][1] + maps[i][j][2]:
                # print("found", cur_seed, "in", maps[i][j])
                # if so, move cur_seed to destination
                offset = cur_seed - maps[i][j][1]
                # if we are going backwards, we need to subtract
                cur_seed = maps[i][j][0] + offset
                break

    # raise Exception("cur_seed", cur_seed)
    final_locs.append(cur_seed)

# print(final_locs)
print(min(final_locs))

# part 2
# each second seed is now the range of the first
seeds2 = []
for i in range(0, len(seeds), 2):
    seeds2.append([])
    seeds2[-1].append(seeds[i])
    seeds2[-1].append(seeds[i + 1])

print(seeds2)

# follow ranges, which split into other ranges
