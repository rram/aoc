#!/usr/bin/python3

import logging

def run(data):
    total = 0
    record = set()
    for line in data:
        for let in line:
            record.add(let)
        if line == "":
            total += len(record)
            record = set()
    return total

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day6.txt") as f:
        data = map(str.strip, f.readlines())

    print(run(data))
