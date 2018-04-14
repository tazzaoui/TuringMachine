#!/usr/env python

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

    def transition(self):
        for transition in self.transitions:
            if transition[0] == self.current_state and transition[1] == self.read():
                self.current_state = transition[2]
                self.write(transition[3])
                self.move(transition[4])

    def execute(self):
        for i in self.tape:
            print(i)

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
