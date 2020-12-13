#!/usr/bin/python3

import logging

def run(data):
    good = 0
    for line in data:
        nums, let, passwd = line.split()
        low, _, high = nums.partition("-")
        low = int(low)
        high = int(high)
        assert let[1] == ":"
        let = let[0]
        if passwd[low-1] == let or passwd[high-1] == let:
            if passwd[low-1] != passwd[high-1]:
                good += 1
    return good


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day2.txt") as f:
        data = f.readlines()

    print(run(data))
