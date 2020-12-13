#!/usr/bin/python3

import logging

def run(data):
    acc = 0
    pc = 0
    hist = []
    while True:
        op, _, val = data[pc].partition(" ")
        val = int(val)

        if pc in hist:
            return acc
        hist.append(pc)

        if op == "nop":
            pass
        elif op == "acc":
            acc += val
        elif op == "jmp":
            pc += val
            continue
        pc += 1


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day8.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
