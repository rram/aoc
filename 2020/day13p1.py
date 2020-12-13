#!/usr/bin/python3

import logging

def run(data):
    t = int(data[0])
    buses = list(map(lambda x: x if x == "x" else int(x), list(data[1].split(","))))
    skip = buses[0]
    logging.info("Checking %r from %i", buses, t)


    wait = None
    bus = None
    for b in filter(lambda x: type(x) == int, buses):
        _, since = divmod(t, b)
        next_bus = b - since
        logging.debug("Next bus %i is at %i", b, t + next_bus)
        if wait is None or next_bus < wait:
            logging.debug("Bus %i is soonest", b)
            wait = next_bus
            bus = b
    return wait * bus



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day13.txt") as f:
        data = list(map(str.strip, f.readlines()))

    while data:
        print(run(data))
        data.pop(0)
        data.pop(0)
