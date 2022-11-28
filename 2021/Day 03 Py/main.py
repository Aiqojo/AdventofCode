import sys
import re
import numpy as np
from collections import defaultdict

def oxygen1(list):
    answer = ''
    for i in range(12):
        zero = 0
        one = 0
        for line in list:
            if line[i] == '0':
                zero += 1
            elif line[i] == '1':
                one += 1
        if zero > one:
            answer += '0'
        else:
            answer += '1'
    return answer


def co1(list):
    answer = ''
    for i in range(12):
        zero = 0
        one = 0
        for line in list:
            if line[i] == '0':
                zero += 1
            elif line[i] == '1':
                one += 1
        if zero < one:
            answer += '0'
        else:
            answer += '1'
    return answer


def oxygen2(list):
    answer = ''
    good_list = []
    for i in range(12):
        zero = 0
        one = 0
        for line in list:
            if line[i] == '0':
                zero += 1
            elif line[i] == '1':
                one += 1
        if zero > one:
            answer += '0'
        elif zero == one:
            answer += '1'
        else:
            answer += '1'
        good_list.clear()
        for line in list:
            # print("SUBSTRING: " + line[0:i+1])
            # print("ANSWER: " + answer)
            if line[i] == answer[i]:
                # print("LINE: " + line)
                good_list.append(line)
                # print("LINE APPENDED: " + str(line))
        list = good_list.copy()
        good_list.clear()
        zero = 0
        one = 0
    return answer


def co2(list):
    answer = ''
    good_list = []
    for i in range(12):
        zero = 0
        one = 0
        for line in list:
            if line[i] == '0':
                zero += 1
            elif line[i] == '1':
                one += 1
        # print("Zero has count: " + str(zero))
        # print("One has count: " + str(one))
        if zero < one:
            answer += '0'
            print(answer)
        elif zero == one:
            answer += '0'
            print(answer)
        else:
            answer += '1'
            print(answer)
        good_list.clear()
        for line in list:
            # print("SUBSTRING: " + line[0:i+1])
            # print("ANSWER: " + answer)
            if line[i] == answer[i]:
                # print("LINE: " + line)
                good_list.append(line)
                # print("LINE APPENDED: " + str(line))
        list = good_list.copy()
        good_list.clear()
        zero = 0
        one = 0
    return answer


def part1(file):
    f = open("aoc_day3.txt", 'r')
    list = []
    for line in f:
        list.append(line.strip())
    print(oxygen1(list))
    print(co1(list))


def part2(file):
    f = open("aoc_day3.txt", 'r')
    list = []
    for line in f:
        list.append(line.strip())
    print(oxygen2(list))
    print(co2(list))


if __name__ == '__main__':
    part1("aoc_day3.txt")
    print("------------")
    part2("aoc_day3.txt")
