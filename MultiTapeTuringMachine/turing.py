#!/usr/env python3

import sys
from transitions import Transition
from transitions import Direction

class TuringMachine:
    def __init__(self, states, transitions, initial_state,
                 accept_state, reject_state, initial_tapes=list(list())):
        self.states = states
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tapes = initial_tapes
        self.heads = list()
        for i in initial_tapes:
            self.heads.append(0)

    def execute(self):
        while not self.halted():
            self.step()

    def step(self):
        for transition in self.transitions:
            if self.current_state == transition.get_origin():
                print("Transitioning!!")
                tapes = transition.get_gamma_origin()
                for i in range(len(self.tapes)):
                    tape = self.read(i)
                    if tape == tapes[i]:
                        self.write(transition.get_gamma_destination()[i], i)
                        self.move(transition.get_directions()[i], i)
                self.current_state = transition.get_destination()
                break

    def halted(self):
        return self.current_state == self.accept_state\
        or self.current_state == self.reject_state
    
    def add_transition(self, transition):
        self.transitions.append(transition)

    def read(self, tape):
        return self.tapes[tape][self.heads[tape]]

    def move(self, direction, tape):
        if direction == Direction.RIGHT:
            self.move_right(tape)
        elif direction == Direction.LEFT:
            self.move_left(tape)

    def move_left(self, tape, steps=1):
        while self.heads[tape] > 0 and steps != 0:
            self.heads[tape] -= 1
            steps -= 1

    def move_right(self, tape, steps=1):
        if len(self.tapes[tape]) < self.heads[tape] + steps:
            for i in range(len(self.tapes[tape]), len(self.tapes[tape]) + steps):
                self.tapes[tape].append(' ')
        self.heads[tape] += steps

    def write(self, char, i):
        if len(self.tapes[i]) < self.heads[i]:
            for i in range(len(self.tapes[i]), len(self.tapes[i]) + self.heads[i]):
                self.tapes[i].append(' ')
        self.tapes[i][self.heads[i]] = char

    def erase(self, i):
        self.tapes[i][self.heads[i]] = None

    def print_transitions(self):
        for transition in self.transitions:
            print(transition)

    def print_tapes(self):
        for i in range(len(self.tapes)):
            self.print_tape(i)

    def print_tape(self, tape):
        for i in self.tapes[tape]:
            sys.stdout.write("[{}]".format(i))
        print('')
