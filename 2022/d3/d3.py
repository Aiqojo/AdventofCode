p = []
f = open("d3.txt", "r")
for line in f:
    p.append(line.strip())

summy1 = 0
summy2 = 0

# a to z is 1 to 26
# capital A to capital Z is 27 to 52
vals = {}
for i in range(1, 27):
    vals[chr(i + 96)] = i
    vals[chr(i + 64)] = i + 26

for i in range(len(p)):
    dd = {}
    ddd = {}
    half = len(p[i]) // 2
    for letter in p[i][:half]:
        # first half
        if letter not in dd:
            dd[letter] = 1
    for letter in p[i][half:]:
        # second half
        if letter not in ddd:
            ddd[letter] = 1
    # both
    for key in dd:
        if key in ddd:
            summy1 += vals[key]
            break

while True:
    l = p[:3]
    d1 = {}
    d2 = {}
    d3 = {}

    print("looking at", l)

    for letter in l[0]:
        if letter not in d1:
            d1[letter] = 1
        else:
            d1[letter] += 1

    for letter in l[1]:
        if letter not in d2:
            d2[letter] = 1
        else:
            d2[letter] += 1

    for letter in l[2]:
        if letter not in d3:
            d3[letter] = 1
        else:
            d3[letter] += 1

    # find the only letter that is in all three
    for letter in d1:
        if letter in d2 and letter in d3:
            print("found", letter, "in all three")
            summy2 += vals[letter]

    p = p[3:]

    if len(p) == 0:
        break

print("Part 1:", summy1)
print("Part 2", summy2)
