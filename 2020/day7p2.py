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


def numChild(mapper, sub):
    assert sub in mapper
    children = 1  # it me
    for cnt, target in mapper[sub]:
        children += int(cnt) * numChild(mapper, target)
    return children


def _my_gen(mapper):
    while True:
        yield mapper

def run(data):
    mapper = genmap(data)
    it = _my_gen(mapper)
    return numChild(mapper, 'shiny gold') - 1
    #return max(map(numChild, it, mapper.keys()))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day7.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
