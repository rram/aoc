#!/usr/bin/python3

import collections
import itertools
import logging

def permutations(mask):
    assert type(mask) == list
    if len(mask) == 0:
        return [""]
    elif mask[0] in ("1", "0"):
        return [mask[0] + rest for rest in permutations(mask[1:])]
    elif mask[0] == "X":
        perms = permutations(mask[1:])
        return ["0" + rest for rest in perms] + ["1" + rest for rest in perms]
    else:
        raise RuntimeException()

def maskval(mask, data):
    assert type(mask) == str, "mask is %s" % type(mask)
    assert type(data) == int, "data is %s" % type(data)
    logging.debug("Data %s (decimal %i)", "{:036b}".format(data), data)
    logging.debug("Mask %s", mask)

    data = "{:036b}".format(data | int(mask.replace("X", "1"), 2))

    res = list(map(lambda bit: bit[1] if bit[1]  == "X" else bit[0], zip(data, mask)))
    logging.debug("Res  %s", "".join(res))
    perms = permutations(res)
    logging.debug("Found %i permutations", len(list(perms)))
    logging.debug("")
    return perms

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
            res = maskval(mask, addr)
            for addr in res:
                memory[int(addr, 2)] = val
        else:
            raise RuntimeException("Error")
    return sum(memory.values())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day14.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
