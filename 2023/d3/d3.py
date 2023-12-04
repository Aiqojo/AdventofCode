import numpy as np
from collections import defaultdict

file = open("d3.txt").read().strip()
with open("d3.txt") as f:
    lines = f.readlines()
    lines = [s.strip() for s in lines]

print(lines)
lines = np.array(lines)
print(lines)

dirs = [(-1, 0), (0, -1), (1, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (0, 1)]

tot = 0
tot2 = 0


default_dict = defaultdict(str)
m_dict = defaultdict(str)

for i, line in enumerate(lines):
    skip_amt = 0
    for j, char in enumerate(line):
        adj = False
        if skip_amt > 0:
            skip_amt -= 1
            continue
        cur_num = ""
        adj_type = ""
        adj_loc = ()

        if char.isdigit():
            while True:
                try:
                    if lines[i][j + skip_amt].isdigit():
                        cur_num += lines[i][j + skip_amt]
                        # print("CUR", cur_num)
                        skip_amt += 1

                        for d in dirs:
                            # check in bounds
                            if (
                                i + d[0] < 0
                                or j + d[1] < 0
                                or i + d[0] >= len(lines)
                                or j + d[1] >= len(lines[0])
                            ):
                                continue

                            for skip_ct in range(skip_amt):
                                if (
                                    lines[i + d[0]][j + d[1] + skip_ct]
                                    not in "0123456789."
                                ):
                                    adj = True
                                    adj_type = lines[i + d[0]][j + d[1] + skip_ct]
                                    # add to dict number and location of adj
                                    adj_loc = (i + d[0], j + d[1] + skip_ct)
                                    # print("LOC", adj_loc)
                                    break

                    else:
                        # print("BROKE NUMBER:", cur_num)
                        break
                except:
                    # print("EXCEPT", cur_num)
                    break

        if adj:
            print("CUR ADDING", cur_num, adj_type)
            if adj_type == "*":
                print("loc in!", cur_num, adj_loc)
                # if dict empty, add to dict
                if adj_loc not in default_dict:
                    default_dict[adj_loc] = int(cur_num)
                    print("ADDED", default_dict)
                    continue
                # if already in dict, multiply by value in dict
                if adj_loc in default_dict:
                    default_dict[adj_loc] *= int(cur_num)
                    # add to multipled dict
                    m_dict[adj_loc] = default_dict[adj_loc]
                    print("ADDED TO M", m_dict)
                    continue

            tot += int(cur_num)

print("\n\n\n\n")


set_combinations = set()

# add all values in multiplied dict to total
for loc in m_dict:
    tot2 += m_dict[loc]

print(tot)
print(tot2)
