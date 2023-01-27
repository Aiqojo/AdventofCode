inp = []
for line in open("t20.txt", "r"):
    inp.append(line.strip())

for num in inp:
    t_num = [n for n in num]
    print(t_num)
