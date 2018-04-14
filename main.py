from transitions import Transition
from transitions import Direction
from turing import TuringMachine

#               s    i    s    0     d
t0 = Transition('0', '1', '2', '1', Direction.LEFT)
t2 = Transition('2', '1', '2', '1', Direction.LEFT)

t0.toggle_start()
t2.toggle_accept()

states = ['0', '2']
transitions = [t0, t2]
initial_state = t0
accept_state = t2
reject_state = None
initial_tape = [0,0,0]

tm = TuringMachine(states, transitions, initial_state, accept_state, reject_state, initial_tape)
tm.execute()
