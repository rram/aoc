#!/usr/bin/python3

import logging

def run(data):
    jolts = sorted(data)
    jolts = [0] + jolts + [max(jolts) + 3]
    one = 0
    tre = 0
    logging.debug("list is %r", jolts)
    for j in jolts:
        o = list(filter(lambda q: q == j+1, jolts))
        one += len(o)
        logging.debug("1 bigger than %i: %r", j, o)
        if not len(o):
            t = list(filter(lambda q: q == j+3, jolts))
            tre += len(t)
            logging.debug("3 bigger than %i: %r", j, t)
    logging.debug("%i bigger by 1", one)
    logging.debug("%i bigger by 3", tre)
    return one * tre

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day10.txt") as f:
        data = list(map(int, map(str.strip, f.readlines())))

    print(run(data))
