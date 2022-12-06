import re

file1 = open('input.txt', 'r')
Lines = file1.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]

for line in Lines:
    string = []
    for sub in line:
        string.append(sub.replace("\n", ""))
    if Lines.index(line) < 8:
        temp = 0
        for x in range(1, 37, 4):
            temp += 1
            if string[x] != ' ':
                stacks[temp-1].append(string[x])
    if string[0] == 'm':
        instructions = re.findall(r'\d+', line)
        #print( '\n' , stacks)
        startpos = (int(instructions[1]))-1
        endpos = (int(instructions[2]))-1
        numCrates = (int(instructions[0]))
        
        temp2 = stacks[startpos][:numCrates]
        del stacks[startpos][:numCrates]
        #print(temp2)
        temp2.reverse()
        for crates in temp2:
            stacks[endpos].insert(0, crates)
        #print(stacks , '\n' )
        #print(stacks)
        #break
    
print(stacks)
print(stacks[0][0], stacks[1][0], stacks[2][0], stacks[3][0], stacks[4][0], stacks[5][0], stacks[6][0], stacks[7][0], stacks[8][0], )