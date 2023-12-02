import numpy as np

lines = []
file = open("d2.txt").read().strip()
with open("d2.txt") as f:
    lines = f.readlines()
    lines = [s.strip().split(" ") for s in lines]

cubes_max = {"red": 12, "green": 13, "blue": 14}
p2 = False
total = 0
total2 = 0
for line in lines:
    print("\n", line)
    cur_amounts = {"red": 0, "green": 0, "blue": 0}
    cur_played = {"red": 0, "green": 0, "blue": 0}
    lline = line[2:]
    for i, val in enumerate(lline):
        if i + 1 == len(lline):
            continue

        cur_val = lline[i + 1].split(":")
        cur_val = cur_val[0].split(",")
        cur_val = cur_val[0].split(";")
        cur_val = cur_val[0]
        over = False
        if val.isdigit():
            if int(val) > cur_amounts[cur_val]:
                print(" NEW VAL", int(val), cur_val)
                cur_amounts[cur_val] = int(val)
                if int(val) > cur_played[cur_val]:
                    cur_played[cur_val] = int(val)
                    print(cur_played)

        for key in cur_amounts:
            if cur_amounts[key] > cubes_max[key]:
                over = True

        if over:
            if p2 == True:
                pass
            else:
                break

        if val[-1] == ";":
            cur_amounts = {"red": 0, "green": 0, "blue": 0}
            print("\n")

    if not over:
        game = line[1].split(":")
        total += int(game[0])

    m = 1
    print(cur_played)
    for key in cur_played:
        m *= cur_played[key]
    print("M", m)

    total2 += m

if not p2:
    print(total)
if p2:
    print(total2)
