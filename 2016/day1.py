#!/usr/bin/python3

import logging

class Stop(Exception):
    pass

class Grid:

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.history = []

    def turn_left(self):
        if self.dir == self.NORTH:
            self.dir = 3
        else:
            self.dir -= 1

    def turn_right(self):
        if self.dir == self.WEST:
            self.dir = 0
        else:
            self.dir += 1

    def move(self, blocks):
        logging.debug("Moving %s %i blocks", self.dirname(), blocks)
        for i in range(blocks):
            if self.dir == self.NORTH:
                self.y += 1
            elif self.dir == self.EAST:
                self.x += 1
            elif self.dir == self.SOUTH:
                self.y -= 1
            elif self.dir == self.WEST:
                self.x -= 1

            coordinate = (self.x, self.y)
            if coordinate in self.history:
                logging.debug("I've been here before")
                raise Stop()

            self.history.append((self.x, self.y))


    def distance(self):
        return abs(self.x) + abs(self.y)

    def dirname(self):
        if self.dir == self.NORTH:
            return "N"
        if self.dir == self.EAST:
            return "E"
        if self.dir == self.SOUTH:
            return "S"
        if self.dir == self.WEST:
            return "W"


def run(data):
    g = Grid()

    for inst in data:
        if inst[0] == "L":
            g.turn_left()
        else:
            g.turn_right()

        try:
            g.move(int(inst[1:]))
            logging.debug("I'm now %i blocks away", g.distance())
        except Stop:
            break

    return g.distance()
            

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = None
    with open("day1.txt") as f:
        for line in f.readlines():
            data = list(map(str.strip, line.split(',')))
            print(run(data))
