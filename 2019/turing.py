#!/usr/bin/python3
import logging

code = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"
code = list(map(int, code.split(",")))

class HaltingException(Exception):
    pass

class Turing():
    def __init__(self, tape):
        self.tape = tape
        self.pc = 0

    def add(self):
        assert self.tape[self.pc] == 1
        in1 = self.tape[self.pc+1]
        in2 = self.tape[self.pc+2]
        out = self.tape[self.pc+3]
        val1 = self.tape[in1]
        val2 = self.tape[in2]
        logging.debug("ADD %i %i #%i", val1, val2, out)
        self.tape[out] = val1 + val2

    def demux(self):
        logging.debug("0x{:02X} %i %i %i %i".format(self.pc),
                *self.tape[self.pc:self.pc+4])
        if self.tape[self.pc] == 1:
            return self.add
        if self.tape[self.pc] == 2:
            return self.multiply
        if self.tape[self.pc] == 99:
            logging.debug("Halting")
            raise HaltingException()
        else:
            raise ValueError("Invalid opcode: %s" % self.tape[self.pc])


    def multiply(self):
        assert self.tape[self.pc] == 2
        in1 = self.tape[self.pc+1]
        in2 = self.tape[self.pc+2]
        out = self.tape[self.pc+3]
        val1 = self.tape[in1]
        val2 = self.tape[in2]
        logging.debug("MUL %i %i #%i", val1, val2, out)
        self.tape[out] = val1 * val2

    def run(self):
        try:
            while True:
                logging.debug(self.tape)
                self.demux()()
                self.pc += 4
        except HaltingException:
            pass
        return self.tape[0]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for noun in range(100):
        for verb in range(100):
            memory = code.copy()
            memory[1] = noun
            memory[2] = verb
            #logging.info("Trying %i %i", noun, verb)
            output = Turing(memory).run()
            if output == 19690720:
                print("%i%i" % (noun, verb))
