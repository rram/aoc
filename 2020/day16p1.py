#!/usr/bin/python3

import logging

def makerule(r1l, r1u, r2l, r2u):
    return lambda x: r1l <= x <= r1u or r2l <= x <= r2u

def run(data):
    section = 0 # rules, mine, nearby
    rules = []
    error = 0
    for line in data:
        if line == "":
            section += 1
            continue

        if section == 0:  # rules
            rule, _, ranges = line.partition(": ")
            r1, _, r2 = ranges.partition(" or ")
            r1l, _, r1u = r1.partition("-")
            r2l, _, r2u = r2.partition("-")
            r1l, r1u, r2l, r2u = map(int, [r1l, r1u, r2l, r2u])
            logging.debug("Adding rule (%s): %i-%i or %i-%i", rule, r1l, r1u, r2l, r2u)
            rules.append(makerule(r1l, r1u, r2l, r2u))
        elif section == 1: # mine
            continue
        elif section == 2: # nearby
            if line == "nearby tickets:":
                continue
            for val in line.split(","):
                val = int(val)
                res = list(map(lambda x: x(val), rules))
                logging.debug(res)
                if not any(res):
                    logging.debug("%i does not match any rules", val)
                    error += val
    return error


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day16.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
