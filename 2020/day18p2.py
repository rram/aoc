#!/usr/bin/python3

import logging

def compute(line):
    logging.debug("Computing %s", line)
    while '(' in line:
        start, end = line.index('(') + 1, None
        inner = 0
        for i, c in enumerate(line[start:]):
            if c == '(':
                inner += 1
            elif c == ')' and inner > 0:
                inner -= 1
            elif c == ')' and inner == 0:
                end = i
                break
        assert end is not None
        sub = line[start:start+end]
        line = line[0:start-1] + compute(sub) + line[start+end+1:]
        logging.debug("Reduced line to %s", line)
    while '+' in line:
        tokens = line.split()
        i = tokens.index('+')
        sub = tokens[i-1:i+2]
        r = str(eval(''.join(sub)))
        line = " ".join(tokens[0:i-1] + [r] + tokens[i+2:])
        logging.debug("Reduced line to %s", line)
    tokens = line.split()
    while len(tokens) != 1:
        assert len(tokens) > 2
        assert tokens[0].isdigit()
        assert tokens[1] in "+-*", repr(tokens[1])
        assert tokens[2].isdigit()
        r = str(eval(''.join(tokens[0:3])))
        tokens = [r] + tokens[3:]
    return tokens[0]


def run(data):
    for line in data:
        logging.debug(" = %s", compute(line))
    return sum(map(int, map(compute, data)))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day18.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
