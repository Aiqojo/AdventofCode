import numpy as np

lines = []
file = open("d1.txt").read().strip()
with open("d1.txt") as f:
    lines = f.readlines()
    lines = [s.strip() for s in lines]

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

p1 = []
p2 = []
for line in lines:
    cur_line1 = ""
    cur_line2 = ""
    # print(line)
    for j, char in enumerate(line):
        if char.isdigit():
            # print("digit", char)
            cur_line1 += char
            cur_line2 += char
        else:
            for thing in nums:
                if line[j:].startswith(thing):
                    # print("word", thing)
                    cur_line2 += str(nums[thing])

    p1.append(cur_line1)
    p2.append(cur_line2)
    # print(cur_line)

r1 = []
for line in p1:
    r1.append(line[0] + line[-1])
r2 = []
for line in p2:
    r2.append(line[0] + line[-1])


su = 0
for v in r1:
    su += int(v)
print(su)


su = 0
for v in r2:
    su += int(v)
print(su)
