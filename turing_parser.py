import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    exit(1)

input_file = list()
tape = list()
line_number = 1
head = 0

with open(sys.argv[1], 'r') as f:
    input_file = f.readlines()

sys.stdout.write("Initial Tape: ")
t = input_file[0].split(' ')[2]
for i in range(len(t) - 1):
    tape.append(t[i])
    sys.stdout.write("[{}]".format(tape[i]))
print('')

while input_file[line_number] != 'done':
    line = input_file[line_number]
    line_split = line.split(' ')
    if line_split[0] == 'move':
        direction = line_split[1].split('\n')[0]
        if direction == 'RIGHT':
            head += 1
        elif direction == 'LEFT':
            if(head > 0):
                head -= 1
    elif line_split[0] == 'if':
        if(tape[head] == line_split[1]):
            direction = line_split[3]
            if direction == 'RIGHT':
                print("Moved RIght")
                head += 1
            elif direction == 'LEFT':
                if(head > 0):
                    head -= 1            
    elif line_split[0] == 'goto':
        line_number = int(line_split[1]) - 1
    elif line_split[0] == 'write':
        tape[head] = line_split[1][0]
    line_number += 1


sys.stdout.write("Output Tape: ")
for i in tape:
    sys.stdout.write("[{}]".format(i))
print('')
