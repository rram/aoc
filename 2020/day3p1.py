#!/usr/bin/python3

import logging

def run(data):
    x, trees = 0, 0
    for line in data[1:]:
        line = line.rstrip()
        x = (x + 3) % len(line)
        if line[x] == "#":
            trees += 1
            line = line[:x] + "X" + line[x+1:]
            line += " HIT"
        else:
            line = line[:x] + "O" + line[x+1:]
        logging.debug(line)
    return trees


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day3.txt") as f:
        data = f.readlines()

    print(run(data))
