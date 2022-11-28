# target area: x=137..171, y=-98..-73

# part 1 is triangle number of abs(lowest point on target) so abs(97) in my case = 4753

# checks if still can hit target
def check(xvel, yvel):
    o_xvel = xvel
    o_yvel = yvel
    xpos = 0
    ypos = 0

    # while it is less than target maximums
    while xpos <= 171 and ypos >= -98:
        if in_target(xpos, ypos):
            print("XPOS:", o_xvel, "YPOS:", o_yvel)
            # returns true if in target, counts as a hit
            return True
        # else, do the calculations
        else:
            xpos += xvel
            ypos += yvel
            if xvel > 0:
                xvel -= 1
            elif xvel < 0:
                xvel += 1
            yvel -= 1

    return False


# checks if in target
def in_target(xpos, ypos):
    if 137 <= xpos <= 171 and -98 <= ypos <= -73:
        return True
    else:
        return False


def main():
    hits = 0
    # looping across all possible ranges
    for xvel in range(17 - 1, 171 + 1):
        for yvel in range(-98 - 1, 98):
            hit = check(xvel, yvel)
            if hit:
                hits += 1
    print(hits)


if __name__ == '__main__':
    main()
