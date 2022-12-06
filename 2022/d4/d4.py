p = []
f = open("t4.txt", "r")
for line in f:
    p.append(line.strip())

c1 = 0
c2 = 0
for i in range(len(p)):
    line = p[i]
    f, b = line.split(",")
    f1, f2 = f.split("-")
    b1, b2 = b.split("-")

    f1 = int(f1)
    f2 = int(f2)
    b1 = int(b1)
    b2 = int(b2)

    if f1 <= b1 and f2 >= b2:
        c1 += 1
    elif b1 <= f1 and b2 >= f2:
        c1 += 1

    # any over lap at all
    if f1 <= b1 and f2 >= b1:
        c2 += 1
    elif b1 <= f1 and b2 >= f1:
        c2 += 1

print(c1, c2)
