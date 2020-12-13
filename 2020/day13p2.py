#!/usr/bin/python3

import functools
import logging

def crt(buses):
    def redmul(it):
        return functools.reduce(int.__mul__, it)
    equivs = [(b - i, b) for i,b in buses]
    product = redmul([modulus for dividend,modulus in equivs])
    Ni = [(int(product/modulus),modulus) for dividend,modulus in equivs]
    xi = [pow(N,modulus-2,modulus) for N,modulus in Ni]
    bNixi = zip([b for b,m in equivs], [N for N,m in Ni], xi)
    x = sum(map(redmul, bNixi))
    return x % product

def test(t, buses):
    for i, b in buses[1:]:
        if (t + i) % b == 0:
            #logging.debug("Bus %i departs at %i", b, t + i)
            pass
        else:
            return False
    return True


def run(data):
    t = int(data[0])
    buses = enumerate(map(lambda x: x if x == "x" else int(x), list(data[1].split(","))))
    buses = list(filter(lambda x: type(x[1]) == int, buses))
    #skip = buses[0]
    logging.info("Checking %r from %i", buses, t)
    #if t % skip != 0:
    #    t -= t % skip
    #while True:
    #    b = [(i, b) for i, b in enumerate(buses) if type(b) == int]
    #    if test(t, b):
    #        return t
    #    t += skip
    #    if t % 1_000_000_000 < skip:
    #        logging.info("t: %i", t)
    #print(buses)
    return crt(buses)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day13.txt") as f:
        data = list(map(str.strip, f.readlines()))

    while data:
        print(run(data))
        data.pop(0)
        data.pop(0)
