import numpy as np
import matplotlib.image

inp = []
for line in open("t15.txt", "r"):
    inp.append(line.strip())

sensors = []
beacons = []

for line in inp:
    l = line.split()
    x1 = l[2][2:-1]
    y1 = l[3][2:-1]
    x2 = l[8][2:-1]
    y2 = l[9][2:]
    sensors.append((int(x1), int(y1)))
    beacons.append((int(x2), int(y2)))

# y_val = 10
y_val = 2000000
on_beacons = 0
for i in range(len(sensors)):
    if sensors[i][1] == y_val:
        on_beacons += 1
        continue


def m_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


print(count)
