file1 = open('input.txt', 'r')
Lines = file1.readlines()

score = 0
dupes = []

for line in Lines:
    currentSack = line.strip()
    firstpart, secondpart = currentSack[:len(currentSack)//2], currentSack[len(currentSack)//2:]
    
    for i in range(len(firstpart)):
        for x in range(len(secondpart)):
            if (firstpart[i] == secondpart[x]) and (firstpart[i] not in dupes):
                dupes.append(firstpart[i])
                if firstpart[i].isupper():
                    score += (ord(firstpart[i]) - 64) + 26
                if firstpart[i].islower():
                    score += (ord(firstpart[i]) - 96)
                
    dupes = []
    
print(score)