#!/usr/bin/python3

import logging

def dist(point):
    return abs(point[0]) + abs(point[1])

def line(data):
    coord = []
    x, y  = 0, 0
    for inst in data.split(","):
        val = int(inst[1:])
        if inst[0] == "R":
            for i in range(val):
                x += 1
                coord.append((x, y))
        elif inst[0] == "U":
            for i in range(val):
                y += 1
                coord.append((x, y))
        elif inst[0] == "L":
            for i in range(val):
                x -= 1
                coord.append((x, y))
        elif inst[0] == "D":
            for i in range(val):
                y -= 1
                coord.append((x, y))
    logging.debug("Coordinates: %r", coord)
    return set(coord)


def run(data):
    l1 = line(data[0])
    l2 = line(data[1])

    u = l1 & l2
    logging.debug("Union: %r", u)

    d = list(map(dist, u))
    logging.debug("Distances: %r", d)
    return min(d)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day3.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
