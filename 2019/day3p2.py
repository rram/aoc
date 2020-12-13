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
    return coord


def run(data):
    l1 = line(data[0])
    l2 = line(data[1])

    u = set(l1) & set(l2)

    def steps(point):
        return l1.index(point) + l2.index(point) + 2

    d = list(map(steps, u))
    return min(d)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day3.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
