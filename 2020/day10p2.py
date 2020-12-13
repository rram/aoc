#!/usr/bin/python3

import logging
from functools import reduce

log = logging.debug

def memoize(fn):
    hist = {}
    def save(args):
        if repr(args) not in hist:
            hist[repr(args)] = fn(args)
        return hist[repr(args)]
    return save

@memoize
def n(data):
    if len(data) == 1:
        logging.debug("We made it to the end")
        return 1

    start, rest = data[0], data[1:]
    res = 0
    if start + 1 in rest:
        res += n(rest[rest.index(start+1):])
        #log("Found %i paths with one: %r", res, rest)
    if start + 2 in rest:
        res += n(rest[rest.index(start+2):])
        #log("Found %i paths with two: %r", res, rest)
    if start + 3 in rest:
        res += n(rest[rest.index(start+3):])
        #log("Found %i paths with tre: %r", res, rest)

    if res == 0:
        #log("Didn't find a path")
        return 0
    return res


def run(data):
    jolts = sorted([0] + data + [max(data) + 3])
    return n(jolts)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = None
    with open("day10.txt") as f:
        data = list(map(int, map(str.strip, f.readlines())))

    print(run(data))
