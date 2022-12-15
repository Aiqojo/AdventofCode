p = []
f = open("t9.txt", "r")
for line in f:
    p.append(line.strip())

cur_pos_head = (0, 0)
prev_pos_head = (0, 0)
cur_pos_tail = (0, 0)
prev_positions_head = {}
prev_positions_tail = {}

prev_positions_head[cur_pos_head] = 1
prev_positions_tail[cur_pos_tail] = 1

cur_line = []
for line in p:
    cur_line = line.split()

    direction = cur_line[0]
    distance = int(cur_line[1])

    for i in range(distance):
        prev_pos_head = cur_pos_head

        if direction == "U":
            cur_pos_head = (cur_pos_head[0], cur_pos_head[1] + 1)
        elif direction == "D":
            cur_pos_head = (cur_pos_head[0], cur_pos_head[1] - 1)
        elif direction == "L":
            cur_pos_head = (cur_pos_head[0] - 1, cur_pos_head[1])
        elif direction == "R":
            cur_pos_head = (cur_pos_head[0] + 1, cur_pos_head[1])

        if cur_pos_head in prev_positions_head:
            prev_positions_head[cur_pos_head] += 1
        else:
            prev_positions_head[cur_pos_head] = 1

        # only move tail if it isnt adjacent to head
        dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
            (0, 0),
        ]
        if cur_pos_head in [
            (cur_pos_tail[0] + d[0], cur_pos_tail[1] + d[1]) for d in dirs
        ]:
            # print("tail didnt move")
            continue
        else:
            cur_pos_tail = prev_pos_head

            # print("tail moved to", cur_pos_tail)

            if cur_pos_tail in prev_positions_tail:
                prev_positions_tail[cur_pos_tail] += 1
            else:
                prev_positions_tail[cur_pos_tail] = 1


print(len(prev_positions_tail))
