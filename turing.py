#!/usr/env python

import sys
from transitions import Transition
from transitions import Direction

class TuringMachine:
    def __init__(self, states, transitions, initial_state,
                 accept_state, reject_state, initial_tape=list()):
        self.states = states
        self.transitions = transitions
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = initial_tape
        self.head = 0

    def execute(self):
        while not self.halted():
            self.step()

    def step(self):
        for transition in self.transitions:
            if self.current_state == transition.get_origin() and\
               self.read() == transition.get_gamma_origin():
                self.write(transition.get_gamma_destination())
                self.current_state = transition.get_destination()
                self.move(transition.get_direction())
                break

    def halted(self):
        return self.current_state == self.accept_state\
        or self.current_state == self.reject_state
    
    def add_transition(self, transition):
        self.transitions.append(transition)

    def read(self):
        return self.tape[self.head]

    def move(self, direction):
        if direction == Direction.RIGHT:
            self.move_right()
        elif direction == Direction.LEFT:
            self.move_left()

    def move_left(self, steps=1):
        while self.head > 0 and steps != 0:
            self.head -= 1
            steps -= 1

    def move_right(self, steps=1):
        self.head += steps

    def write(self, char):
        self.tape[self.head] = char

    def erase(self):
        self.tape[self.head] = None

    def print_transitions(self):
        for transition in self.transitions:
            print(transition)

    def print_tape(self):
        for i in self.tape:
            sys.stdout.write("[{}]".format(i))
        print('')


