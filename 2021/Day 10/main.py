import numpy as np

def sum_illegal(file):
    scores = []
    f = open(file, 'r')
    totals = {}
    totals[')'] = 0
    totals[']'] = 0
    totals['}'] = 0
    totals['>'] = 0
    for l in f:
        cur_chunk = ''
        for ch in l:
            valid = True
            if ch == '\n':
                break
            if ch == '(' or ch == '[' or ch == '{' or ch == '<':
                cur_chunk+=ch
            else:
                if cur_chunk[-1] == '(':
                    if ch == ')':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        totals[ch]+=1
                        valid = False
                        break
                elif cur_chunk[-1] == '[':
                    if ch == ']':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        totals[ch]+=1
                        valid = False
                        break
                elif cur_chunk[-1] == '{':
                    if ch == '}':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        totals[ch]+=1
                        valid = False
                        break
                elif cur_chunk[-1] == '<':
                    if ch == '>':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        totals[ch]+=1
                        valid = False
                        break

            if valid:
                score = 0
                for char in cur_chunk[::-1]:
                    score = 5 * score
                    print(char)
                    if char == "(":
                        score+=1
                    elif char == "[":
                        score+=2
                    elif char == "{":
                        score+=3
                    elif char == "<":
                        score+=4
                scores.append(score)

    scores = sorted(scores)
    print(scores[len(scores)//2])

    #     if valid:
    #         val = 0
    #         for ch in cur_chunk[::-1]:
    #             val = val*5
    #             if ch == '(':
    #                 val+=1
    #             elif ch == '[':
    #                 val+=2
    #             elif ch == '{':
    #                 val+=3
    #             else:
    #                 val+=4
    #         scores.append(val)
    # scores = sorted(scores)
    # print(scores[len(scores) // 2])




    # res = 3*totals[')'] + 57*totals[']'] + 1197*totals['}'] + 25137*totals['>']
    # print(res)

def sum_completions(file):
    f = open(file, 'r')
    scores = []
    for l in f:
        cur_chunk = ''
        for ch in l:
            valid = True
            if ch == '\n':
                break
            if ch == '(' or ch == '[' or ch == '{' or ch == '<':
                cur_chunk+=ch
            else:
                if cur_chunk[-1] == '(':
                    if ch == ')':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        valid = False
                        break
                elif cur_chunk[-1] == '[':
                    if ch == ']':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        valid = False
                        break
                elif cur_chunk[-1] == '{':
                    if ch == '}':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        valid = False
                        break
                elif cur_chunk[-1] == '<':
                    if ch == '>':
                        cur_chunk = cur_chunk[0:-1]
                    else:
                        valid = False
                        break
        if valid:
            val = 0
            for ch in cur_chunk[::-1]:
                val = val*5
                if ch == '(':
                    val+=1
                elif ch == '[':
                    val+=2
                elif ch == '{':
                    val+=3
                else:
                    val+=4
            scores.append(val)
    scores = sorted(scores)
    print(scores[len(scores) // 2])


def part1(filename):
    f = open(filename, 'r')
    total = 0
    totals = [0]*4
    points = [3,57,1197,25137]
    opens = "([{<"
    closes = ")]}>"
    para = 0
    bracket = 0
    curly = 0
    v = 0
    cchar = ""
    currentline = ""


    for line in f:
        charr = ""
        for i in line.strip():
            totals = [0]*4
            if i == "(":
                # totals[0] += 1
                cchar += i
            elif i == ")":
                print("in )")
                if not cchar.endswith("("):
                    total += 3
                    break
                else:
                    charr = charr[:-1]
                # totals[0] -= 1
            elif i == "[":
                # totals[1] += 1
                cchar += i
            elif i == "]":
                print("in ]")
                if not cchar.endswith("["):
                    total += 57
                    break
                else:
                    charr = charr[:-1]
                # totals[1] -= 1
            elif i == "{":
                # totals[2] += 1
                cchar += i
            elif i == "}":
                print("in }")
                if not cchar.endswith("{"):
                    total += 1197
                    break
                else:
                    charr = charr[:-1]
                # totals[2] -= 1
            elif i == "<":
                # totals[3] += 1
                cchar += i
            elif i == ">":
                print("in >")
                if not cchar.endswith("<"):
                    total += 25137
                    break
                else:
                    charr = charr[:-1]
                # totals[3] -= 1
            # for k in range(4):
            #     counter = 0
            #     if totals[k] < 0:
            #         if k == 0:
            #             total += 3
            #         elif k == 1:
            #             total += 57
            #         elif k == 2:
            #             total += 1197
            #         else:
            #             total += 25137
    print(total)

# bad 25976928 10336995 622962


def main():
    sum_illegal("aoc_day10.txt")
    sum_completions("aoc_day10.txt")


if __name__ == '__main__':
    main()
