p = []
f = open("t9.txt", "r")
for line in f:
    p.append(line.strip())

directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def move(p, d):
    return p[0] + d[0], p[1] + d[1]


size = 2

rope = [(0, 0)] * size
visited = set(rope)

for line in p:
    d, dist = line.split()
    dist = int(dist)

    for i in range(dist):
        rope[0] = move(rope[0], directions[d])
        for rope in range(1, len(rope)):
            delta = [rope[rope - 1][i] - rope[rope][i] for i in (0, 1)]
            if abs(max(delta, ropeey=abs)) > 1:
                rope[rope] = move(rope[rope], [x // (abs(x) or 1) for x in delta])
        visited.add(rope[-1])

print(len(visited))
