import numpy as np
from collections import defaultdict, deque

# create a dict to keep track of edges
connections = defaultdict(list)


# setting up connections
def setup(file):
    global connections
    f = open(file, 'r')
    for line in f:
        a, b = line.strip().split("-")
        # this records what node is connected to what other nodes
        connections[a].append(b)
        # do the reverse too because if a is connected to b, the reverse must be true
        connections[b].append(a)


# a set is unordered list of objects, im using it to hold previous caves for a specific search
def part1(curr, past=set()):
    # since the path has to start at "start" it will return all the way back to total here and I can print it out
    total = 0
    # if it is "end" return 1 cause path is finished
    if curr == "end":
        return 1
    # if it is lowercase (small cave) and hasn't been visited continue, else stop, you can't visit a small cave twice
    if curr.lower() == curr:
        if curr in past:
            return 0
    # this is new, "|" is a union between both sets
    past = past | {curr}
    # for each other connection from the current node, test those paths recursively
    for cave in connections[curr]:
        total += part1(cave, past)
    return total


# keeps track of part for part two, but  mostly same logic
def part2(curr, part, past=set()):
    total = 0
    if curr == "end":
        return 1
    if curr.lower() == curr and curr in past:
        # had the check again to make sure curr wasn't start, I think small caves led back to it
        if curr == "start":
            return 0
        # if part is 2, set it to 1, so it doesn't double up on the same small cave again
        if part == 2:
            part = 1
        else:
            return 0
    past = past | {curr}
    for cave in connections[curr]:
        total += part2(cave, part, past)
    return total


def main():
    setup("aoc_day12.txt")
    print(part1("start", set()))
    print(part2("start", 2, set()))


if __name__ == '__main__':
    main()
