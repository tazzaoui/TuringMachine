"""
This file is used for testing the Turing Machine Simulator
"""

from transitions import Transition
from transitions import Direction
from turing import TuringMachine


def test_write():

    """
    Ensure transitions correctly write to the tape
    """

    # If(state == 0 and tape == 1 then go to state 1, write 0 & move right)
    t0 = Transition('0', '1', '1', '0', Direction.RIGHT)
    t0.toggle_start()

    #If(state == 1 and tape == 0 then go to state 2, write 1 & move right)
    t1 = Transition('1', '0', '2', '1', Direction.RIGHT)

    # If(state == 2 and tape == 1 then go to state 3, write 1 & move right)
    t2 = Transition('2', '1', '3', '0', Direction.RIGHT)

    # Halt at 3
    t3 = Transition('3', None, None, None, None)
    t3.toggle_accept()

    tm = TuringMachine(['0', '1', '2', '3'],
                       [t0, t1, t2, t3],
                       '0', '3', None,
                       ['1', '0', '0', '0'])

    tm.step()
    assert tm.tape == ['0', '0', '0', '0'], 'Failed to correctly write to tape'

    tm.step()
    assert tm.tape == ['0', '1', '0', '0'], 'Failed to correctly write to tape'

    tm.step()
    assert tm.tape == ['0', '1', '0', '0'], 'Failed to correctly write to tape'

    tm.step()
    assert tm.tape == ['0', '1', '0', '0'], 'Failed to correctly write to tape'


if "__name__" == "__main__":
    test_write()
