p = []
f = open("t2.txt", "r")
for line in f:
    p.append(line.strip())
# 0 lost 3 draw 6 won
s1 = 0
s2 = 0

for line in p:
    l = line.split(" ")
    L1 = l[0]
    L2 = l[1]
    # a = rock, b = paper, c = scissors
    # x = rock, y = paper, z = scissors
    # 6 for win, 3 for draw, 0 for lost
    # +1 rock +2 paper +3 scissors
    ### part 1
    if L2 == "X":
        s1 += 1
    elif L2 == "Y":
        s1 += 2
    elif L2 == "Z":
        s1 += 3

    if L1 == "A":  # they picked rock
        if L2 == "Y":
            s1 += 6
        elif L2 == "Z":
            s1 += 0
        else:
            s1 += 3
    elif L1 == "B":  # they picked paper
        if L2 == "Z":
            s1 += 6
        elif L2 == "X":
            s1 += 0
        else:
            s1 += 3
    elif L1 == "C":  # they picked scissors
        if L2 == "X":
            s1 += 6
        elif L2 == "Y":
            s1 += 0
        else:
            s1 += 3

    # a = rock, b = paper, c = scissors
    # now x = lose, y = draw, z = win
    # +1 for rock, +2 for paper, +3 for scissors
    ### part 2
    if L1 == "A":
        if L2 == "X":  # lose - pick scissors
            s2 += 0 + 3
        elif L2 == "Y":  # draw - pick rock
            s2 += 3 + 1
        elif L2 == "Z":  # win - pick paper
            s2 += 6 + 2
    elif L1 == "B":
        if L2 == "X":  # lose - pick rock
            s2 += 0 + 1
        elif L2 == "Y":  # draw - pick paper
            s2 += 3 + 2
        elif L2 == "Z":  # win - pick scissors
            s2 += 6 + 3
    elif L1 == "C":
        if L2 == "X":  # lose - pick paper
            s2 += 0 + 2
        elif L2 == "Y":  # draw - pick scissors
            s2 += 3 + 3
        elif L2 == "Z":  # win - pick rock
            s2 += 6 + 1

print(s1, s2)
f.close()
