from enum import Enum

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    STAY = 2

class Transition:
    def __init__(self, origin, gamma_origin, destination,
                 gamma_destination, direction):
        self.origin = origin
        self.gamma_origin = gamma_origin
        self.destination = destination
        self.gamma_destination = gamma_destination
        self.direction = direction
        self.is_start = False
        self.is_accept = False
        self.is_reject = False

    def get_origin(self):
        return self.origin

    def get_gamma_origin(self):
        return self.gamma_origin

    def get_destination(self):
        return self.destination

    def get_gamma_destination(self):
        return self.gamma_destination

    def get_direction(self):
        return self.direction

    def toggle_start(self):
        self.is_start = not self.is_start

    def toggle_accept(self):
        self.is_accept = not self.is_accept

    def toggle_reject(self):
        self.is_reject = not self.is_reject
