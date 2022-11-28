import numpy as np
import matplotlib.pyplot as plt

paper = []
inst = []
fold_count = 0
matches = 0

def part1(file, instructions):
    global inst
    global paper
    global matches
    f = open(file, 'r')
    for line in f:
        paper.append(line.strip().split(","))
    # print(paper)
    ff = open(instructions, 'r')
    for line in ff:
        inst.append(line.strip().split("="))
    # print(inst)

    #getmaxmin()

    # for ii in range(len(ff)):
    #     paper = fold(paper, ff[ii])
    for ii in list(inst):
        paper = fold(paper, ii)
    plot(paper)
    print((paper))




def plot(paper):
    # if i change paper to set i can do this, taken from liejurv
    # ys = [pos[1] for pos in paper]
    # xs = [pos[0] for pos in paper]
    # for y in range(min(ys), max(ys) + 1):
    #     s = ""
    #     for x in range(min(xs), max(ys) + 1):
    #         if (x, y) in paper:
    #             s += "X"
    #         else:
    #             s += " "
    # print(s)

    for i in paper:
        plt.scatter(int(i[0]), int(i[1])*-1)
    plt.show()


def fold(paper, ins):
    global ff
    global fold_count
    global matches
    matched = []
    for i in list(paper):
        if ins[0] == "y":
            if int(i[1]) > int(ins[1]):
                # print("INSTRUCTIONS: ", ins)
                # print("IN Y: ", i)
                i[1] = int(i[1]) - (int(i[1]) - (int(ins[1])))*2
                # print("OUT Y: ", i)
        elif ins[0] == "x":
            if int(i[0]) > int(ins[1]):
                # print("INSTRUCTIONS: ", ins)
                # print("IN X: ", i)
                i[0] = int(i[0]) - (int(i[0]) - (int(ins[1])))*2
                # print("OUT X: ", i)

    counter = 0
    for i in list(paper):
        for k in list(paper):
            # print(i,k)
            if int(i[0]) == int(k[0]) and int(i[1]) == int(k[1]):
                if counter == 0:
                    counter+=1
                else:
                    matched.append(k)
                    paper.remove(k)
        counter = 0
        same = False
    print(len(paper))
    for i in range (0,len(paper)):
        paper[i][0] = int(paper[i][0])
        paper[i][1] = int(paper[i][1])




    return paper


if __name__ == '__main__':
    # part1("test.txt", "test2.txt")
    part1("13.txt", "instruc.txt")
