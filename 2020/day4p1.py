#!/usr/bin/python3

import logging

REQUIRED_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

OPTIONAL_FIELDS = [
    "cid",
]

def run(data):
    num_valid = 0
    record = {}
    for line in data:
        logging.debug("processing '%s'", line)
        if not line:
            logging.debug("Record complete %r", record)
            if set(record.keys()) == set(REQUIRED_FIELDS):
                logging.debug("Found valid passport")
                num_valid += 1
            record = {}
            continue

        fields = line.split()
        for f in fields:
            k, _, v = f.partition(":")
            if k in REQUIRED_FIELDS:
                record[k] = v
            else:
                logging.debug("Ignoring invalid field: %s", k)

    return num_valid


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day4.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
