#!/usr/bin/python3

import logging

def run(data):
    total = 0
    records = []
    for line in data:
        if line == "":
            logging.debug(records)
            fold = records[0]
            for r in records:
                fold &= r
            
            total += len(fold)

            records = []
        else:
            records.append(set(line))
    return total

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day6.txt") as f:
        data = map(str.strip, f.readlines())

    print(run(data))
