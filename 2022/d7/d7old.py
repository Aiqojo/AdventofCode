p = []
f = open("t7.txt", "r")
for line in f:
    p.append(line.strip())

dirs = {}

cur_dir = ""
what_in = []

i = 0
while True:
    if i >= len(p):
        break

    line = p[i].split()

    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                cur_dir = cur_dir[: cur_dir.rfind("/")]
            elif line[2] != "/":
                cur_dir += "/" + line[2]

        elif line[1] == "ls":
            # read in following lines until next $ command
            while True:
                i += 1
                if i >= len(p):
                    break
                if p[i][0] == "$":
                    break
                what_in.append(p[i])

            # going through each folder/file in current directory
            for w in what_in:
                ww = w.split()
                # if dir, add to dirs
                if ww[0] == "dir":
                    if cur_dir not in dirs:
                        dirs[cur_dir] = 0
                else:
                    # add ww[0] (file size) to all parent directories
                    cur = cur_dir
                    while cur != "":
                        if cur in dirs:
                            dirs[cur] += int(ww[0])
                            print(cur, dirs[cur])
                        else:
                            dirs[cur] = int(ww[0])
                            print(cur, dirs[cur])
                        # move back one dir by removing last "/" and folder name preceeding it
                        cur = cur[: cur.rfind("/")]

            what_in = []

    i += 1
    if i == len(p):
        break

# for d in dirs:
#     print(dirs[d], d)

print(sum([dirs[d] for d in dirs if dirs[d] < 100000]))
