#!/usr/bin/python3

import collections
import logging

def maskval(mask, data):
    assert type(mask) == str, "mask is %s" % type(mask)
    assert type(data) == int, "data is %s" % type(data)
    logging.debug("Data %s (decimal %i)", "{:036b}".format(data), data)
    logging.debug("Mask %s", mask)

    on = int(mask.replace("X", "0"), 2)
    data |= on

    off = int(mask.replace("X", "1"), 2)
    data &= off
    logging.debug("Res  %s (decimal %i)", "{:036b}".format(data), data)
    logging.debug("")
    return data

def run(data):
    memory = collections.defaultdict(int)
    mask = None
    while data:
        line = data.pop(0)
        if line.startswith("mask"):
            #logging.debug("Memory dump: %r", memory)
            mask = line[7:]
            assert len(mask) == 36, "%r (%i)" % (mask, len(mask))
        elif line.startswith("mem"):
            addr = int(line[4:line.index("]")])
            val = int((line.partition(" = "))[2])
            res = maskval(mask, val)
            memory[addr] = res
        else:
            raise RuntimeException("Error")
    logging.debug("Memory dump: %r", memory)
    return sum(memory.values())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day14.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
