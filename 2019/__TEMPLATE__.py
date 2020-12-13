#!/usr/bin/python3

import logging

def run(data):
    pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("dayN.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
