#!/usr/bin/python3

import logging

from functools import reduce

WLEN = 25
TARGET = 1212510616

def run(data):
    for i in range(len(data)):
        for j in range(i+2,len(data)):
            tot = reduce(lambda x,y: x+y, data[i:j])
            if tot == TARGET:
                logging.debug("Found range: %r", data[i:j])
                return min(data[i:j]) + max(data[i:j])
            if tot > TARGET:
                break


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day9.txt") as f:
        data = list(map(int, map(str.strip, f.readlines())))

    print(run(data))
