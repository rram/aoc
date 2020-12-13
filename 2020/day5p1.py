#!/usr/bin/python3

import logging

def seatID(code):
    code = code.replace('F', '0')
    code = code.replace('B', '1')
    code = code.replace('L', '0')
    code = code.replace('R', '1')

    row = int(code[:7], 2)
    column = int(code[7:], 2)
    return row * 8 + column

def run(data):
    return max(map(seatID, data))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day5.txt") as f:
        data = map(str.strip, f.readlines())

    print(run(data))
