#!/usr/bin/python3

import logging

def run(data):
    total = 1
    xstep = [1, 3, 5, 7, 1]
    ystep = [1, 1, 1, 1, 2]
    for xs, ys in zip(xstep, ystep):
        x, y, trees = 0, 0, 0
        for line in data[1:]:
            y += 1
            if y % ys != 0:
                continue

            line = line.rstrip()
            x = (x + xs) % len(line)
            if line[x] == "#":
                trees += 1
                line = line[:x] + "X" + line[x+1:]
                line += " HIT"
            else:
                line = line[:x] + "O" + line[x+1:]
            logging.debug(line)
        logging.info("%i trees hit", trees)
        total *= trees
        logging.info("Total is now %i", total)

    return total


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = None
    with open("day3.txt") as f:
        data = f.readlines()

    print(run(data))
