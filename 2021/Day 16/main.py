parse_set = {
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
    'F': '1111'
}


def part1(file):
    global parse_set

    f = open(file, 'r')
    message = ''
    for line in f:
        message = line.strip()

    print(message)
    message = "".join([parse_set[x] for x in message])
    print(message)
    print("991")
    print("1264485568252")


def something(data):
    global parse_set
    version = int(data[:3], 2)
    message = data[:3]
    version_total = 0
    version_total += int(version)

    type_id = int(message[:3], 2)

    if type_id == 4:
        loop = True
        literal_value = ''
        while loop:
            type_id = message[0]
            literal_value += message[1:5]
            message = message[:5]
            if type_id == '0':
                loop = False
    else:
        length_type_id = message[:1]
        message = message[1:]
        if length_type_id == "0":
            data = message[:15]
            message = message[15:]

        elif length_type_id == "1":
            return "these nuts"




def main():
    part1("test.txt")


if __name__ == '__main__':
    main()
