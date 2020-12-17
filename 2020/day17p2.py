#!/usr/bin/python3

import collections
import logging

class Point(collections.namedtuple("Point", ['x', 'y', 'z', 'w'])):
    def __lt__(self, other):
        if self.z < other.z and self.y < other.y and self.x < other.x and self.w < other.w:
            return True
        return False


class Space(object):

    def __init__(self):
        self.cycles = 0
        self.min = Point(0,0,0,0)
        self.max = Point(0,0,0,0)
        self.matter = collections.defaultdict(bool)

    def __str__(self):
        logging.debug("Min %s", self.min)
        logging.debug("Max %s", self.max)
        if self.cycles == 0:
            res = "Before any cycles:\n"
        elif self.cycles == 1:
            res = "After 1 cycle:\n"
        else:
            res = "After {} cycles:\n".format(self.cycles)

        y, z, w = None, None, None
        for p in self:
            if z is None or p.z != z or p.w != w:
                z = p.z
                w = p.w
                res += "\nz={} w={}".format(z, w)
            if y is None or p.y != y:
                y = p.y
                res += "\n"
            res += "#" if self[p] else "."
        return res + "\n"

    def __getitem__(self, key):
        assert isinstance(key, Point)
        return self.matter[key]
    
    def __setitem__(self, key, value):
        assert isinstance(key, Point)
        self.matter[key] = value
        if key < self.min:
            self.min = key
        elif key > self.max:
            self.max = key

    def __iter__(self):
        for z in range(self.min.z, self.max.z+1):
            for y in range(self.min.y, self.max.y+1):
                for x in range(self.min.x, self.max.x+1):
                    for w in range(self.min.w, self.max.w+1):
                        yield Point(x, y, z, w)

    def neighbors(self, point):
        res = []
        for z in (-1, 0, 1):
            for y in (-1, 0, 1):
                for x in (-1, 0, 1):
                    for w in (-1, 0, 1):
                        if Point(x, y, z, w) == Point(0, 0, 0, 0):
                            continue
                        else:
                            t = Point(point.x+x, point.y+y, point.z+z, point.w+w)
                            res.append(self[t])
        return res


    def cycle(self):
        bang = collections.defaultdict(bool, self.matter)
        if self.cycle == 0:
            self.min.z = -1
            self.max.z = 1
            self.min.w = -1
            self.max.w = 1
        else:
            self.min = Point(self.min.x-1, self.min.y-1, self.min.z-1, self.min.w-1)
            self.max = Point(self.max.x+1, self.max.y+1, self.max.z+1, self.max.w+1)

        for p in self:
            ncount = self.neighbors(p).count(True)
            if self[p]:
                bang[p] = True if ncount in (2, 3) else False
            elif ncount == 3:
                bang[p] = True
        self.matter = bang
        self.cycles += 1

    def count(self):
        return len(list(filter(bool, self.matter.values())))


def run(data):
    space = Space()
    for y, line in enumerate(data):
        for x, spot in enumerate(line):
            p = Point(x, y, 0, 0)
            space[p] = True if spot == "#" else False
    print(space)

    while space.cycles < 6:
        space.cycle()
        
        if space.cycles < 4:
            print(space)

    return space.count()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day17.txt") as f:
        data = list(map(str.strip, f.readlines()))

    print(run(data))
