#!/usr/bin/python3

import logging

from copy import deepcopy


def numAdjOcc(chart, x, y):
    num = 0
    for j in (-1, 0, 1):
        for i in (-1, 0, 1):
            if (i, j) == (0,0):
                continue
            if x + i < 0 or x + i == len(chart[0]):
                continue
            if y + j < 0 or y + j == len(chart):
                continue
            if chart[y+j][x+i] == "#":
                num += 1
    return num


def doRound(data):
    chart = deepcopy(data)
    for y, line in enumerate(data):
        for x, spot in enumerate(line):
            if spot == ".":
                continue
            adjOcc = numAdjOcc(data, x, y)
            logging.debug("Spot (%i,%i): %s Adjacent: %i", x, y, spot, adjOcc)
            if spot == "L" and adjOcc == 0:
                chart[y][x] = "#"
            elif spot == "#" and adjOcc > 3:
                chart[y][x] = "L"
        logging.debug("Prev: %s", "".join(data[y]))
        logging.debug("New : %s", "".join(chart[y]))
    return chart


def printChart(chart):
    for line in chart:
        print("".join(line))
    print()

def numOcc(line):
    return line.count("#")

def run(data):
    printChart(data)
    res, last = 0, -1
    r = 0
    while res != last:
        data = doRound(data)
        #printChart(data)
        res, last = sum(map(numOcc, data)), res
        r += 1
        logging.info("Round %i: %i", r, res)

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = None
    with open("day11.txt") as f:
        data = list(map(list, map(str.strip, f.readlines())))

    print(run(data))
