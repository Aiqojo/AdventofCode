p = []
f = open("t6.txt", "r")
for line in f:
    p.append(line.strip())

for line in p:
    counter = 0
    listt = []
    size = 4
    # size = 14
    for letter in line:
        if counter < size:
            listt.append(letter)
            counter += 1
        else:   
            d = set(listt)
            if len(d) == size:
                print(counter)
                break
            else:
                listt.pop(0)
                listt.append(letter)
                counter += 1
