#!/usr/bin/python3

import logging

def run(nums):
    turn = 0
    history = {}
    new, prev = None, None
    for i in nums:
        prev = history.get(i)
        history[i] = turn
        turn += 1

    for i in range(turn, 30_000_000):
        #logging.debug(history)
        if prev is not None:
            new = turn - prev - 1
            #logging.debug("TURN %i OLD inserting %i", turn+1, new)
        else:
            new = 0
            #logging.debug("TURN %i NEW inserting %i", turn+1, new)
        prev = history.get(new)
        history[new] = turn
        turn += 1
        logging.debug("TURN %i PREV is %r", turn+1, prev)
        #if turn % 1_000_000 == 0:
            #logging.info("TURN %i", turn+1)
    return new


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = None
    with open("day15.txt") as f:
        data = list(map(str.strip, f.readlines()))
    for line in data:
        print(run(list(map(int, line.split(",")))))
