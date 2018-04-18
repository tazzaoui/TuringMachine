#!/usr/bin/python3

import sys

def print_tape(tape):
    for i in tape:
        sys.stdout.write("[{}]".format(i))
    print('')

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    exit(1)

input_file = list()
tape = list()
line_number = 1
head = 0

with open(sys.argv[1], 'r') as f:
    input_file = f.readlines()

print("Reading {}...".format(sys.argv[1]))
print("Read in {} instructions...\n".format(len(input_file)))

t = input_file[0].split(' ')[2]
for i in range(len(t) - 1):
    tape.append(t[i])


while input_file[line_number] != "done":
    line = input_file[line_number]
    line_split = line.split(" ")
    if line_split[0] == "move":
        direction = line_split[1].split("\n")[0]
        if direction == "RIGHT":
            head += 1
        elif direction == "LEFT":
            if(head > 0):
                head -= 1
    elif line_split[0] == "if":
        if(tape[head] == line_split[1]):
            direction = line_split[3]
            if direction == "RIGHT":
                print("Moved RIght")
                head += 1
            elif direction == "LEFT":
                if(head > 0):
                    head -= 1            
    elif line_split[0] == "goto":
        line_number = int(line_split[1]) - 1
    elif line_split[0] == "write":
        tape[head] = line_split[1][0]
    elif line_split[0].strip('\n') == "print":
        print_tape(tape)
    elif line_split[0].strip('\n') == "halt":
        print("Halted Execution")
        exit(1)
    else:
        print("Unrecognized syntax on line {} \n {}".format(line_number, line))
        exit(1)
    line_number += 1

