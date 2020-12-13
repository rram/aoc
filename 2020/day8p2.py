#!/usr/bin/python3

import logging
import time

def run(data):
    acc = 0
    pc = 0
    hist = []
    while True:
        if pc == len(data):
            return acc
        if pc in hist:
            raise RuntimeException("Infinite Loop")
        hist.append(pc)
        op, _, val = data[pc].partition(" ")
        val = int(val)
        logging.debug("PC: %s, ACC: %s, %s", pc, acc, data[pc])

        if op == "nop":
            pass
        elif op == "acc":
            acc += val
        elif op == "jmp":
            pc += val
            continue
        pc += 1


def runall(data):
    for lineno in range(len(data)):
        op, _, val = data[lineno].partition(" ")

        if op == "nop":
            try:
                return run(data[0:lineno] + ["jmp %s" % (val)] + data[lineno+1:])
            except:
                pass
        elif op == "jmp":
            try:
                return run(data[0:lineno] + ["nop %s" % (val)] + data[lineno+1:])
            except:
                pass
        else:
            continue


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day8.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(runall(data))
