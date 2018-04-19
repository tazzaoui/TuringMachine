from transitions import Transition
from transitions import Direction
from turing import TuringMachine

t0 = Transition("0", ("0", "0", "0"), "2", ("1", "4", "7"), [Direction.RIGHT, Direction.RIGHT, Direction.RIGHT])
t2 = Transition("2", ("0", "0", "0"), "3", ("2", "5", "8"), [Direction.RIGHT, Direction.RIGHT, Direction.RIGHT])
t3 = Transition("3", ("0", "0", "0"), "4", ("3", "6", "9"), [Direction.RIGHT, Direction.RIGHT, Direction.RIGHT])
t4 = Transition("4", ("2", "5", "8"), "4", ("3", "6", "9"), [Direction.RIGHT, Direction.RIGHT, Direction.RIGHT])

t0.toggle_start()
t4.toggle_accept()

states = ["0", "2", "3", "4"]
transitions = [t0, t2, t3, t4]
initial_state = "0"
accept_state = "4"
reject_state = None
initial_tape = [['0','0','0'], ['0','0','0'], ['0','0','0']]

tm = TuringMachine(states, transitions, initial_state, accept_state, reject_state, initial_tape)

print("Tansitions....")
tm.print_transitions()
print("Initial tapes...")
tm.print_tapes()
tm.execute()
print("Final tapes...")
tm.print_tapes()
