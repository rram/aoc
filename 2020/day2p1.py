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
        if low <= passwd.count(let) <= high:
            logging.debug("%s has %i %s's and is GOOD", passwd, passwd.count(let), let)
            good += 1
        else:
            logging.debug("%s has %i %s's and is BAD", passwd, passwd.count(let), let)
    return good


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day2.txt") as f:
        data = f.readlines()

    print(run(data))
