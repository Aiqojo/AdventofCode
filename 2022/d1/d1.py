import os

p = []
f = open("t1.txt", "r")

for line in f:
    p.append(line.strip())

# uncomment for part 1
# mx = [0]
# uncomment for part 2
mx = [0, 0, 0]
cur = 0
indx = 0
for line in p:
    if line == "":
        if min(mx) < cur:
            mx[mx.index(min(mx))] = cur
        indx += 1
        cur = 0
    else:
        cur += int(line)

print(sum(mx))
