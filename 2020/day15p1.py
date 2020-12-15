#!/usr/bin/python3

import logging

def run(nums):
    nums.reverse()
    for i in range(len(nums), 2020):
        logging.debug("TURN %i %r", i+1, nums)
        if nums[0] not in nums[1:]:
            nums.insert(0, 0)
            logging.info("TURN %i NEW inserting 0", i+1)
        else:
            prev = nums.index(nums[0], 1)
            nums.insert(0, prev)
            logging.info("TURN %i OLD inserting %i", i+1, prev)
    return nums[0]


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    data = None
    with open("day15.txt") as f:
        data = list(map(str.strip, f.readlines()))
    for line in data:
        print(run(list(map(int, line.split(",")))))
