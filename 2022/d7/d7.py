p = []
f = open("t7.txt", "r")
for line in f:
    p.append(line.strip())

d = {}
with open("t7.txt") as f:
    cd = "/"
    ls = []
    for line in f:
        l = line.strip()
        if l[0] == "$":
            if l[0:5] == "$ cd ":

                if not len(ls) == 0:
                    d[cd] = tuple(ls)
                ls = []

                opt = l.split()[2]
                if opt == "/":
                    cd = "/"
                elif opt == "..":
                    cd = cd[0 : cd[0:-2].rindex("/") + 1]
                else:
                    cd += opt + "/"
            continue
        ls.append(l)
    if not len(ls) == 0:
        d[cd] = tuple(ls)

dirs = d
print(dirs)


def get_folder_size(folder):
    size = 0
    if not folder in dirs:
        return 0
    for f in dirs[folder]:
        if f[0] == "d":
            size += get_folder_size(folder + f.split()[1] + "/")
        else:
            size += int(f.split()[0])

    return size


print(dirs)


s = 0
for f in dirs.keys():
    s_temp = get_folder_size(f)
    if s_temp <= 100000:
        s += s_temp

print(s)

minny = 999999999999999999999
target = 30000000 - (70000000 - get_folder_size("/"))

for f in dirs.keys():
    s_temp = get_folder_size(f)
    if s_temp >= target and s_temp < minny:
        minny = s_temp

print(minny)
