#!/usr/bin/python3

import logging
import re

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
    raw = []
    for line in data:
        if not line:
            logging.debug("Record complete %r", record)
            if set(record.keys()) == set(REQUIRED_FIELDS):
                logging.debug("Found valid passport")
                num_valid += 1
                print(" ".join(raw))
            record = {}
            raw = []
            continue

        fields = line.split()
        for f in fields:
            raw.append(f)
            k, _, v = f.partition(":")
            if k in REQUIRED_FIELDS:
                if k == "byr" and not 1920 <= int(v) <= 2002:
                    logging.debug("Invalid byr: %s", v)
                    continue
                if k == "iyr" and not 2010 <= int(v) <= 2020:
                    logging.debug("Invalid iyr: %s", v)
                    continue
                if k == "eyr" and not 2020 <= int(v) <= 2030:
                    logging.debug("Invalid eyr: %s", v)
                    continue
                if k == "hgt":
                    if v[-2:] == "cm":
                        if not 150 <= int(v[:-2]) <= 193:
                            logging.debug("Invalid hgt: %s", v)
                            continue
                    elif v[-2:] == "in":
                        if not 59 <= int(v[:-2]) <= 76:
                            logging.debug("Invalid hgt: %s", v)
                            continue
                    else:
                        logging.debug("Invalid hgt: %s", v)
                        continue
                if k == "hcl":
                    if not re.match("#[0-9a-f]{6}", v):
                        logging.debug("Invalid hcl: %s", v)
                        continue
                if k == "ecl" and v not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    logging.debug("Invalid ecl: %s", v)
                    continue
                if k == "pid":
                    if not len(v) == 9 or not all(map(lambda n: bool(int(n)+1), v)):
                        logging.debug("Invalid pid: %s", v)
                        continue
                record[k] = v
            else:
                #logging.debug("Ignoring invalid field: %s", k)
                pass

    return num_valid


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = None
    with open("day4.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
