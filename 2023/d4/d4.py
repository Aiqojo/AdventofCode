import numpy as np
from collections import defaultdict

file = open("e4.txt").read().strip()
with open("e4.txt") as f:
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
    # print(line)
    win = line[0].split(":")
    win = win[1].split()
    wins.append(win)
    have = line[1].split()
    haves.append(have)
    # print(win)
    # print(have)

    # finding the number of winning numbers I have
    count = 0
    cur_tot = 0

    for num in have:
        if num in win:
            count += 1
            if cur_tot == 0:
                cur_tot = 1
            else:
                cur_tot *= 2

    # print()
    tot += cur_tot

print(tot)

file = open("d4.txt").read().strip()
with open("d4.txt") as f:
    lines = f.readlines()
    lines = [s.strip() for s in lines]

lines = np.array(lines)
win = None
have = None

copies = defaultdict(int)
copies_2 = defaultdict(int)
tot_2_2 = 0
for i, line in enumerate(lines):
    if i % 2 == 0:
        print(i)
    # print()
    line = line.split("|")
    # print(line)
    win = line[0].split(":")
    win = win[1].split()
    have = line[1].split()

    while True:
        count = 0

        for num in have:
            if num in win:
                count += 1

        tot_2_2 += 1

        for j in range(count):
            # print(i + j + 2)
            copies[i + j + 1] += 1
            copies_2[i + j + 1] += 1

        # if the first game, break
        if i == 0:
            break

        if copies[i] == 0:
            break

        # if there are still copies for this game, continue
        if copies[i] > 0:
            copies[i] -= 1

print(tot_2_2)
