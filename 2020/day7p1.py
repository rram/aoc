#!/usr/bin/python3

import logging
import re

a = re.compile(r'(\w+ \w+) bags contain ')
b = re.compile(r'(\d+) (\w+ \w+) bags?(\.|, )')
END = "."


def genmap(data):
    num = 0
    mapper = {}
    for line in data:
        m = a.match(line)
        assert m
        sub = m.group(1)
        target = []

        while m:
            line = line[len(m.group(0)):]
            if line == "no other bags.":
                break
            m = b.match(line)
            assert m
            target.append(m.group(1, 2))
            if m.group(3) == END:
                break

        mapper[sub] = target
    return mapper


def canHold(mapper, sub):
    assert sub in mapper
    for cnt, target in mapper[sub]:
        if target == "shiny gold":
            return True
        if canHold(mapper, target):
            return True
    return False


def run(data):
    mapper = genmap(data)
    
    possible = [t for t in mapper.keys() if canHold(mapper, t)]
    return len(possible)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day7.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
