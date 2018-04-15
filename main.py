from transitions import Transition
from transitions import Direction
from turing import TuringMachine

t0 = Transition("0", "1", "2", "6", Direction.RIGHT)
t2 = Transition("2", "6", "2", "7", Direction.RIGHT)

t0.toggle_start()
t2.toggle_accept()

states = ["0", "2"]
transitions = [t0, t2]
initial_state = "0"
accept_state = "2"
reject_state = None
initial_tape = ['1','1','0']

tm = TuringMachine(states, transitions, initial_state, accept_state, reject_state, initial_tape)

tm.print_transitions()
tm.print_tape()
tm.execute()
tm.print_transitions()
tm.print_tape()
