#!/usr/bin/python3

import logging
import math

def dist(x, y):
    return abs(x) + abs(y)

def run(data):
    sx, sy =  0, 0
    wx, wy = 10, 1
    for line in data:
        a = line[0]
        c = int(line[1:])

        if   a == "N":
            wy += c
        elif a == "S":
            wy -= c
        elif a == "E":
            wx += c
        elif a == "W":
            wx -= c
        elif a == "L" or a == "R":
            xdiff = wx - sx
            ydiff = wy - sy
            logging.debug("Diff is (%i, %i)", xdiff, ydiff)
            if a == "R":
                c *= -1
            r = math.radians(c)
            xshift = xdiff * round(math.cos(r)) - ydiff * round(math.sin(r))
            yshift = xdiff * round(math.sin(r)) + ydiff * round(math.cos(r))
            logging.debug("Shift is (%i, %i)", xshift, yshift)
            wxp = xshift + sx
            wyp = yshift + sy
            wx, wy = wxp, wyp
        elif a == "F":
            xdiff = wx - sx
            ydiff = wy - sy
            for i in range(c):
                sx, sy = wx, wy
                wx += xdiff
                wy += ydiff
        else:
            assert False
        logging.debug("Ins: %s (%i, %i) (%i, %i)", line, sx, sy, wx, wy)

    return dist(sx, sy)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day12.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
