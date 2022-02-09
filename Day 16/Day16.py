sum_version_nums = 0


def interpret_part_one(file):
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'}
    f = open(file, 'r')
    num = f.readline()
    # num = 'A0016C880162017C3686B18A3D4780'
    message = ''
    for ch in num:
        message += hex_to_bin[ch]
    print(num)
    print(message)
    res = interpret(message)
    global sum_version_nums
    print(sum_version_nums)
    print('Decoded: ' + str(res))


def interpret(message):
    print('----------------------')
    version = message[:3]
    global sum_version_nums
    sum_version_nums += int(version, 2)
    type_id = message[3:6]
    rest = message[6:]
    print(version + ', ' + type_id)
    print(rest)
    if type_id == '100':
        print('literal')
        end_term = rest[len(rest) - len(rest) % 5:]
        segments = [rest[i:i + 5] for i in range(0, len(rest) - len(rest) % 5, 5)]
        res = ''
        remaining = ''
        ok = True
        for segment in segments:
            if ok:
                res += segment[1:]
                if segment[0] == '0':
                    ok = False
            else:
                remaining += segment
        remaining += end_term
        print('remaining: ' + remaining)
        print(int(res, 2))
        return int(res, 2), remaining
    else:
        if rest[0] == '0':
            print('operator 0')
            length = int(rest[1:16], 2)
            print(rest[1:16] + ', ' + rest[16:])
            print('length: ' + str(length))
            rest = rest[16:]
            remaining = rest[length:]
            print(remaining)
            # placeholder operation
            if type_id == '000':
                res = 0
                while rest != remaining:
                    print(rest)
                    evaluation = interpret(rest)
                    res += evaluation[0]
                    rest = evaluation[1]
            elif type_id == '001':
                res = 1
                while rest != remaining:
                    print(rest)
                    evaluation = interpret(rest)
                    res *= evaluation[0]
                    rest = evaluation[1]
            elif type_id == '010':
                evs = []
                while rest != remaining:
                    print(rest)
                    evaluation = interpret(rest)
                    evs.append(evaluation[0])
                    rest = evaluation[1]
                evs.sort()
                res = evs[0]
            elif type_id == '011':
                evs = []
                while rest != remaining:
                    print(rest)
                    evaluation = interpret(rest)
                    evs.append(evaluation[0])
                    rest = evaluation[1]
                evs.sort()
                res = evs[-1]
            elif type_id == '101':
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                if first > second:
                    res = 1
            elif type_id == '110':
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                if first < second:
                    res = 1
            else:
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                if first == second:
                    res = 1
            print('remaining: ' + remaining)
            return res, remaining
        else:
            print('operator 1')
            number_of_subs = int(rest[1:12], 2)
            print(str(rest[1:12]) + ', ' + str(rest[12:]))
            print('number: ' + str(number_of_subs))
            rest = rest[12:]
            # operations
            if type_id == '000':
                res = 0
                for _ in range(number_of_subs):
                    print(rest)
                    evaluation = interpret(rest)
                    res += evaluation[0]
                    rest = evaluation[1]
            elif type_id == '001':
                res = 1
                for _ in range(number_of_subs):
                    print(rest)
                    evaluation = interpret(rest)
                    res *= evaluation[0]
                    rest = evaluation[1]
            elif type_id == '010':
                evs = []
                for _ in range(number_of_subs):
                    print(rest)
                    evaluation = interpret(rest)
                    evs.append(evaluation[0])
                    rest = evaluation[1]
                evs.sort()
                res = evs[0]
            elif type_id == '011':
                evs = []
                for _ in range(number_of_subs):
                    print(rest)
                    evaluation = interpret(rest)
                    evs.append(evaluation[0])
                    rest = evaluation[1]
                evs.sort()
                res = evs[-1]
            elif type_id == '101':
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                rest = evaluation[1]
                if first > second:
                    res = 1
            elif type_id == '110':
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                rest = evaluation[1]
                if first < second:
                    res = 1
            else:
                res = 0
                evaluation = interpret(rest)
                first = evaluation[0]
                rest = evaluation[1]
                evaluation = interpret(rest)
                second = evaluation[0]
                rest = evaluation[1]
                if first == second:
                    res = 1
            print('remaining: ' + rest)
            return res, rest


def main():
    interpret_part_one("16.txt")


if __name__ == '__main__':
    main()
