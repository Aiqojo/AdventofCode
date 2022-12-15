import numpy as np
from matplotlib import pyplot as plt

p = []
f = open("t10.txt", "r")
for line in f:
    p.append(line.strip())

grid = []
for i in range(6):
    grid.append([0] * 40)

instr = {"noop": 1, "addx": 2}
inst_count = 0
val = 1
temp_val = val
fin_sum = 0
sprite_center = 1
vals = []
vals.append(val)

for i in range(0, len(p)):
    p[i] = p[i].split(" ")
    p[i][0] = instr[p[i][0]]
    if len(p[i]) == 2:
        p[i][1] = int(p[i][1])
    for j in range(0, p[i][0]):
        inst_count += 1
        # print("cycle num", inst_count)
        if len(p[i]) == 2 and j == 1:
            # print(val, "+", p[i][1], "=", val + p[i][1])
            val += p[i][1]
        if inst_count == 20 or (inst_count - 20) % 40 == 0:
            # print("adding", val, "*", inst_count, "=", val * inst_count)
            fin_sum += temp_val * inst_count
        temp_val = val
        vals.append(val)

for i in range(240):
    t = vals[i] - (i % 40)
    if abs(t) <= 1:
        grid[i // 40][i % 40] = 1

grid = np.array(grid)
plt.imshow(grid, cmap="gray")
plt.savefig("d10.png")
print(fin_sum)
