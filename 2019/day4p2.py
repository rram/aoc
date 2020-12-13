#!/usr/bin/python3

import logging

def wrap(fn):
    def log(arg):
        arg = str(arg)
        res = fn(arg)
        if res:
            pass
        return res
    return log

@wrap
def test(pwd):
    pwd = str(pwd)
    m = pwd[0]
    r = 0
    nr = 0
    for i in pwd:
       if i < m:
           return False
       elif i == m:
           r += 1
           if r == 2:
               nr += 1
           if r == 3:
               nr -= 1
       else:
           m = i
           r = 1

    if nr == 0:
        print(pwd)
        return False
    if len(set(pwd)) == 6:
        return False
    return True

def run(data):
    lower, _, upper = data[0].partition("-")
    lower = int(lower)
    upper = int(upper)

    return len(list(filter(test, range(lower, upper+1))))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day4.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
