#!/usr/bin/python3

import logging

from collections import deque

WLEN = 25


def is_valid(window):
    assert len(window) == WLEN + 1
    logging.debug("Checking for %i", window[-1])
    for i in range(WLEN):
        for j in range(WLEN):
            if i == j:
                continue

            tot = window[i] + window[j]
            if tot == window[-1]:
                logging.debug("%i + %i = %i", window[i], window[j], window[-1])
                return True
    logging.info("No match")
    return False


def run(data):
    window = deque([])
    for line in data:
        window.append(int(line))
        if len(window) > WLEN:
            if is_valid(window):
                window.popleft()
            else:
                return line

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day9.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
