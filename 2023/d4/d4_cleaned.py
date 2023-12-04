import numpy as np
from collections import defaultdict

file = open("d4.txt").read().strip()
with open("d4.txt") as f:
    lines = f.readlines()
    lines = [s.strip() for s in lines]

lines = np.array(lines)
print(lines)

win = None
have = None
wins = []
haves = []
tot = 0

for i, line in enumerate(lines):
    line = line.split("|")
    win = line[0].split(":")[1].split()
    have = line[1].split()

    # finding the count of winning numbers I have
    cur_tot = 0

    for num in have:
        if num in win:
            if cur_tot == 0:
                cur_tot = 1
            else:
                cur_tot *= 2

    tot += cur_tot

print("part1:", tot)  # 19855


copies = defaultdict(int)
copies_2 = defaultdict(int)
tot2 = 0
for i, line in enumerate(lines):
    if i % 5 == 0:
        print(i)

    line = line.split("|")
    win = line[0].split(":")[1].split()
    have = line[1].split()

    while True:  # loop over each copy
        tot2 += 1  # each loop here means +1 total card

        count = 0  # keeps track of same numbers
        for num in have:
            if num in win:
                count += 1

        # adding copies
        for j in range(count):
            copies[i + j + 1] += 1
            copies_2[i + j + 1] += 1

        # if the first game or out of copies, break
        if i == 0 or copies[i] == 0:
            break

        # if there are still copies for this game, continue
        copies[i] -= 1

print(tot2)  # 10378710
