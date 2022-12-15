import numpy as np
from matplotlib import pyplot as plt
import functools

p = []
f = open("t11.txt", "r")
for line in f:
    p.append(line.strip())

monkeys = []
ops = []
tests = []
div = []
t_throw = []
f_throw = []

for line in p:
    if line.startswith("Starting items: "):
        _ = line[16:].split(", ")
        t = []
        for i in _:
            t.append(int(i))
        monkeys.append(t)
    elif line.startswith("Operation: "):
        ops.append(line[17:])
    elif line.startswith("Test: divisible by "):
        tests.append(int(line[19:]))
    elif line.startswith("If true: throw to monkey "):
        t_throw.append(int(line[24:]))
    elif line.startswith("If false: throw to monkey "):
        f_throw.append(int(line[25:]))

godmod = 1
for d in tests:
    godmod *= d


def monkey_mul(item, op):
    ret = 0
    if op == "old * old":
        ret = item * item
    elif op.startswith("old * "):
        ret = item * int(op[6:])
    elif op.startswith("old + "):
        ret = item + int(op[6:])
    # return int(ret / 3)
    return ret


looks = [0] * len(monkeys)
looks = np.array(looks)
looks = looks.astype(np.int64)
# for i in range(20):
for i in range(10000):
    # print(i)
    t_monkeys = [[] for _ in range(len(monkeys))]
    for i, monkey in enumerate(monkeys):
        for item in monkey:
            looks[i] += 1
            new_item = monkey_mul(item, ops[i])
            new_item = new_item % godmod
            if new_item % tests[i] == 0:
                t_monkeys[t_throw[i]].append(new_item)
            else:
                t_monkeys[f_throw[i]].append(new_item)

        # check if there are new items in t_monkeys on [i+1]
        # if so, add to monkeys[i+1]
        if i + 1 < len(monkeys):
            if len(t_monkeys[i + 1]) > 0:
                monkeys[i + 1].extend(t_monkeys[i + 1])
                t_monkeys[i + 1] = []

    monkeys = t_monkeys
    # print("LOOKS", looks)

looks = np.sort(looks)
print(looks[-1] * looks[-2])
