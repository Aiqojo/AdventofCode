import numpy as np
from collections import defaultdict

file = open("d1.txt").read().strip()
with open("d1.txt") as f:
    lines = f.readlines()
    lines = [s.strip().split("   ") for s in lines]

lines = np.array(lines).astype(int)

f_col = np.sort(lines[:, 0])
s_col = np.sort(lines[:, 1])

print(f_col)
print(s_col)

tot = 0

for i in range(len(f_col)):
    tot += abs(f_col[i] - s_col[i])

print(tot)

# p2
f_counts = defaultdict(int)
s_counts = defaultdict(int)

for i in range(len(f_col)):
    f_counts[f_col[i]] += 1
    s_counts[s_col[i]] += 1

tot_2 = 0

for v in f_col:
    if v in s_counts:
        tot_2 += v * s_counts[v]

print(tot_2)
