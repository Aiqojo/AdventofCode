import sys
import re
import numpy as np
from collections import defaultdict


def part1(file):
    # Finding how many 1s, 4s, 7s, and 8s are present in the outputs
    f = open(file, 'r')
    total = 0
    for line in f:
        # Split the line and only look at the last 4 phrases
        s = line.split('|')[1].strip()
        nums = s.split(' ')
        for n in nums:
            # If its 2 long, its 1
            if len(n.strip()) == 2: total += 1
            # If its 4 long, its 4
            if len(n.strip()) == 4: total += 1
            # If its 3 long, its 7
            if len(n.strip()) == 3: total += 1
            # If its 7 long, its 8
            if len(n.strip()) == 7: total += 1
    print("PART 1: " + str(total))


# Counting how many letters each phrase shares
def count_letters(phrase):
    # Storing char counts in dict
    chars1 = defaultdict(int)
    chars2 = defaultdict(int)

    for char in phrase[0]:
        chars1[char] += 1
    for char in phrase[1]:
        chars2[char] += 1

    same = 0
    for char in chars1:
        if chars1[char] == chars2[char]:
            same += 1
    # Returns amount of shared letters
    return same


# Does the decoding and figures out which phrase matches to which number
def decode(phrase):
    total = ''
    s = phrase.split(' ')
    input = s[:10]
    output = s[11:]

    for n in input:
        # Copying 1, 4, 7, and 8 to compare to later
        if len(n) == 2:
            one = n
        elif len(n) == 4:
            four = n
        elif len(n) == 3:
            seven = n
        elif len(n) == 7:
            eight = n

    for n in output:
        # Same as part 1 for 1, 4, 7, and 8, but also adding it to a string
        if len(n) == 2:
            total += '1'
        elif len(n) == 4:
            total += '4'
        elif len(n) == 3:
            total += '7'
        elif len(n) == 7:
            total += '8'
        # If the length is 5, it can either be 3, 5, or 2
        elif len(n) == 5:
            # 3 shares 2 chars with 1
            if count_letters([n, one]) == 2:
                total += '3'
            # 5 shares 3 chars with 4
            elif count_letters([n, four]) == 3:
                total += '5'
            # Otherwise, 2
            else:
                total += '2'
        # If the length is 6, it can either be 9, 0, or 6
        elif len(n) == 6:
            # 9 shares 4  chars with 4
            if count_letters([n, four]) == 4:
                total += '9'
            # 0 shares 3 chars with 7
            elif count_letters([n, seven]) == 3:
                total += '0'
            # Otherwise, 6
            else:
                total += '6'
        print("OUTPUT: " + str(n) + " | DECODED: " + total)
    print("LINE TOTAL: " + total)
    # Turn that string to int and we good
    return int(total)


if __name__ == '__main__':
    part1("aoc_day8.txt")
    f = open("aoc_day8.txt", 'r')
    s = 0
    counter = 1
    for line in f:
        print("LINE: " + str(counter))
        counter += 1
        s += decode(line.strip())
        print("CURR TOTAL: " + str(s) + "\n")
    print(s)
