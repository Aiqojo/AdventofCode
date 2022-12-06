p = []
f = open("t5.txt", "r")
for line in f:
    p.append(line.strip())

one = ["q", "w", "p", "s", "z", "r", "h", "d"]
two = ["v", "b", "r", "w", "q", "h", "f"]
three = ["c", "v", "s", "h"]
four = ["p", "g", "j", "b", "z"]
five = ["p", "g", "j", "b", "z"]
six = ["q", "t", "j", "h", "w", "f", "l"]
seven = ["z", "t", "w", "d", "l", "v", "j", "n"]
eight = ["d", "t", "z", "c", "j", "g", "h", "f"]
nine = ["w", "p", "v", "m", "b", "h"]

listt = [one, two, three, four, five, six, seven, eight, nine]

pp = []
for i in range(0, len(p)):
    linee = [int(x) for x in p[i].split() if x.isdigit()]
    pp.append(linee)

for n in pp:
    count = n[0]
    while count > 0:
        # uncomment for part 1
        val = listt[n[1] - 1].pop()
        # uncomment for part 2
        # val = listt[n[1] - 1].pop(-count)
        listt[n[2] - 1].append(val)
        count -= 1

for i in range(0, len(listt)):
    print(listt[i][-1].upper(), end="")
