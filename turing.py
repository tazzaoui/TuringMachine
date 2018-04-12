#!/usr/env python

import enum

class Direction(enum.Enum):
    RIGHT = 1
    LEFT = 2
    STAY = 3

class Turing:
    def __init__(self, states, delta, initial_state,
                 accept_state, reject_state, initial_tape):
        self.states = states
        self.delta = delta
        self.current_state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = initial_tape
        self.head = 0

    def transition(self):
        for transition in self.delta:
            if transition[0] == self.current_state and transition[1] == self.read():
                self.current_state = transition[2]
                self.write(transition[3])
                self.move(transition[4])

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
