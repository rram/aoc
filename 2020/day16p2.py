#!/usr/bin/python3

import collections
import logging


def makerule(r1l, r1u, r2l, r2u):
    return lambda x: r1l <= x <= r1u or r2l <= x <= r2u


def validticket(rules, values):
    for val in values:
        if not any(list(map(lambda x: x(val), rules))):
            return False
    return True


def run(data):
    section = 0 # rules, mine, nearby
    rules = {}
    mine = []
    nearby = []
    mapping = {}
    for line in data:
        if line == "":
            section += 1
            continue

        if section == 0:  # rules
            rule, _, ranges = line.partition(": ")
            r1, _, r2 = ranges.partition(" or ")
            r1l, _, r1u = r1.partition("-")
            r2l, _, r2u = r2.partition("-")
            r1l, r1u, r2l, r2u = map(int, [r1l, r1u, r2l, r2u])
            logging.debug("Adding rule (%s): %i-%i or %i-%i", rule, r1l, r1u, r2l, r2u)
            rules[rule] = makerule(r1l, r1u, r2l, r2u)
        elif section == 1: # mine
            if line == "your ticket:":
                continue
            mine = list(map(int, line.split(",")))
        elif section == 2: # nearby
            if line == "nearby tickets:":
                continue
            values = list(map(int, line.split(",")))
            if not validticket(rules.values(), values):
                logging.debug("%s is invalid", line)
                continue
            nearby.append(values)
        else:
            raise RuntimeException()

    possible_index = collections.defaultdict(list)
    for rulename in rules.keys():
        logging.debug("testing %s", rulename)
        for i in range(len(rules)):
            if all(map(lambda x: rules[rulename](x), [ticket[i] for ticket in nearby])):
                possible_index[rulename].append(i)
    logging.debug(possible_index)

    while possible_index:
        to_purge = None
        for rulename, indicies in possible_index.items():
            if len(indicies) == 1:
                logging.debug("%s is field %i", rulename, indicies[0])
                mapping[rulename] = indicies[0]
                assert to_purge is None
                to_purge = (rulename, indicies[0])
                break
        
        assert to_purge is not None
        del possible_index[to_purge[0]]
        for rulename, indicies in possible_index.items():
            if to_purge[1] in indicies:
                indicies.remove(to_purge[1])

    logging.debug("Mapping is %i", len(mapping))
    logging.debug("rules is %i", len(rules))
    if len(mapping) + 1 == len(rules):
        assert False
        missing_index = set(range(len(rules))) - set(mapping.values())
        for rule in rules.keys():
            if rule not in mapping:
                mapping[rule] = missing_index
                break

    assert len(mapping) == len(rules)

    res = 1
    for name, index in mapping.items():
        if name.startswith("departure"):
            res *= mine[index]

    return res


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day16.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
