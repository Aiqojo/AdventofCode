from collections import Counter
from collections import defaultdict

arr = []


def initialize_rules(file):
    rules = {}
    f = open(file, 'r')
    for line in f:
        l = line.strip().split(' -> ')
        rules[l[0]] = l[1]
    return rules


def initialize_rules_upgraded(file):
    rules = {}
    f = open(file, 'r')
    for line in f:
        l = line.strip().split(' -> ')
        rules[l[0]] = [l[0][0] + l[1], l[1] + l[0][1]]
    return rules


def part1(file):
    rules = initialize_rules_upgraded(file)
    simple_rules = initialize_rules(file)
    num_of_pair = defaultdict(int)

    polymer = "OFSVVSFOCBNONHKFHNPK"
    totals = defaultdict(int)
    for ch in polymer:
        totals[ch] += 1
    for i in range(len(polymer) - 1):
        key = polymer[i:i + 2]
        num_of_pair[key] += 1

    num = 474747474747
    num_close = 1000000000000000000000000000000000000000000000000000000000000
    range_set = 0

    for k in range(500000):
        temp_pairs = defaultdict(int)
        for key in num_of_pair.keys():
            temp_pairs[rules[key][0]] += num_of_pair[key]
            temp_pairs[rules[key][1]] += num_of_pair[key]
            totals[simple_rules[key]] += num_of_pair[key]
        num_of_pair = temp_pairs.copy()

    values = sorted(totals.values())
    print(values[-1] - values[0])


def main():
    part1("14.txt")


if __name__ == '__main__':
    main()
