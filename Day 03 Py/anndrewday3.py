import sys
import re

def gamma(filename):
  f = open(filename, 'r')
  ones = [0,0,0,0,0,0,0,0,0,0,0,0]
  tot = 0
  for line in f:
    entry = re.search(r'\d+', line)
    num = entry.group()
    tot = tot + 1
    for i in range(len(num)):
      if num[i] == '1':
        ones[i] = ones[i] + 1
  res = ''
  for d in ones:
    if d > tot/2:
      res = res + '1'
    else:
      res = res + '0'
  return res



def epsilon(filename):
  g = gamma(filename)
  res = ''
  for i in range(len(g)):
    if g[i] == '0':
      res = res + '1'
    else:
      res = res + '0'
  return res

def multiply_bin(x, y):
    print(int(x,2))
    print(int(y,2))
    return int(x, 2) * int(y, 2)


def Oxy(filename):
    g = gamma(filename)
    f = open(filename, 'r')
    nums = f.readlines()
    index = 0
    for i in range(len(nums)):
        nums[i] = '@' + nums[i]
    while len(nums) > 1:
        cringe = G(nums)
        key = '@' + cringe[0:index]
        delete = []
        for i in range(len(nums)):
            if not key in nums[i]:
                delete.append(i)
        for i in range(len(delete)):
            nums.pop(delete[i] - i)
        index = index + 1
    res = nums[0][1:-1]
    print(nums)
    return res


def CO(filename):
    g = epsilon(filename)
    f = open(filename, 'r')
    nums = f.readlines()
    index = 0
    for i in range(len(nums)):
        nums[i] = '@' + nums[i]
    prev = '@'
    while len(nums) > 1:
        cringe = E(nums)
        key = prev + cringe[index]
        prev = key
        delete = []
        for i in range(len(nums)):
            if not key in nums[i]:
                delete.append(i)
        for i in range(len(delete)):
            nums.pop(delete[i] - i)
        index = index + 1
        print('hi')
        print(key)
    res = nums[0][1:-1]
    return res


def G(nums):
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in nums:
        d = re.search(r'\d+', n)
        dab = d.group()
        for i in range(len(dab)):
            if dab[i] == '1':
                ones[i] = ones[i] + 1
    res = ''
    for d in ones:
        if d >= len(nums) / 2:
            res = res + '1'
        else:
            res = res + '0'
    return res


def E(nums):
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in nums:
        d = re.search(r'\d+', n)
        dab = d.group()
        for i in range(len(dab)):
            if dab[i] == '1':
                ones[i] = ones[i] + 1
    res = ''
    for d in ones:
        if d >= len(nums) / 2:
            res = res + '0'
        else:
            res = res + '1'
    print(res)
    return res


def main():
    args = sys.argv[1:]
    if args[0] == '--mode2':
        print(multiply_bin(Oxy(args[1]), CO(args[1])))
    else:
        print(multiply_bin(gamma(args[0]), epsilon(args[0])))


if __name__ == '__main__':
    main()