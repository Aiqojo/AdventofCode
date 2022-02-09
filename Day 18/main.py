import ast



def main(file):
    f = open(file, 'r')
    lines  = f.readlines()
    cur = ast.literal_eval(lines[0].strip())
    for l in lines[1:]:
        #num = ast.literal_eval(l.strip())
        num = l.strip()
        cur = reduce([cur, num])
        print(cur)
    res = magnitude(cur)
    print(res)
    f.close()



def reduce(arr):
    line = arr[1]
    complete = False
    exploded = False
    split = False

    open_bracket = 0

    while not complete:
        for char in line:
            if char == "[":
                open_bracket += 1
            elif char == "]":
                open_bracket -= 1

            if open_bracket == 5:
                left = int(char+1)
                right = int(char+3)






        if not exploded and not split:
            complete = True



if __name__ == '__main__':
    main("test.txt")
