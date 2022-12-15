p = []
f = open("t8.txt", "r")
for line in f:
    p.append(line.strip())

count = 0
for i in range(len(p)):
    for j in range(len(p[i])):
        cur = int(p[i][j])
        # check if visible to the left
        # get all numbers to the left
        left = [*p[i][:j]]
        # make all ints
        left = [int(x) for x in left]
        if len(left) > 0:
            if cur > max(left):
                count += 1
                continue
        else:
            count += 1
            continue
        # check if visible to the right
        # get all numbers to the right
        right = [*p[i][j + 1 :]]
        # make all ints
        right = [int(x) for x in right]
        if len(right) > 0:
            if cur > max(right):
                count += 1
                continue
        else:
            count += 1
            continue
        # check if visible above
        # get all numbers above
        above = []
        for k in range(i):
            above.append(int(p[k][j]))
        if len(above) > 0:
            if cur > max(above):
                count += 1
                continue
        else:
            count += 1
            continue
        # check if visible below
        # get all numbers below
        below = []
        for k in range(i + 1, len(p)):
            below.append(int(p[k][j]))
        if len(below) > 0:
            if cur > max(below):
                count += 1
                continue
        else:
            count += 1
            continue

print(count)

p = []
f = open("t8.txt", "r")
for line in f:
    p.append(line.strip())

count = 0
scores = []
for i in range(len(p)):
    for j in range(len(p[i])):
        cur = int(p[i][j])
        dist_l = 1
        dist_r = 1
        dist_u = 1
        dist_b = 1

        # get numbers from the left going out from the current position
        left = [*p[i][:j]]
        left = [int(x) for x in left]
        left = left[::-1]
        for k in range(len(left)):
            if left[k] >= cur:
                break
            else:
                dist_l += 1

            if k == max(range(len(left))):
                dist_l -= 1

        # get numbers from the right going out from the current position
        right = [*p[i][j + 1 :]]
        right = [int(x) for x in right]
        for k in range(len(right)):
            if right[k] >= cur:
                break
            else:
                dist_r += 1

            if k == max(range(len(right))):
                dist_r -= 1

        # get numbers from above going out from the current position
        above = []
        for k in range(i):
            above.append(int(p[k][j]))
        above = above[::-1]
        for k in range(len(above)):
            if above[k] >= cur:
                break
            else:
                dist_u += 1

            if k == max(range(len(above))):
                dist_u -= 1

        # get numbers from below going out from the current position
        below = []
        for k in range(i + 1, len(p)):
            below.append(int(p[k][j]))
        for k in range(len(below)):
            if below[k] >= cur:
                break
            else:
                dist_b += 1

            if k == max(range(len(below))):
                dist_b -= 1

        # print(cur, dist_l, dist_r, dist_u, dist_b)
        scores.append(dist_l * dist_r * dist_u * dist_b)

print(max(scores))
