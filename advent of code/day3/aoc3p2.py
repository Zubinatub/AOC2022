file1 = open('input.txt', 'r')
Lines = file1.readlines()

score = 0
strings = []
dupes = []

for line in Lines:
    currentSack = line.strip()
    strings.append(currentSack)
    if len(strings) == 3:
        for i in range(len(strings[0])):
            if (strings[0][i]) in strings[1] and (strings[0][i]) in strings[2] and strings[0][i] not in dupes:
                dupes.append(strings[0][i])
                if strings[0][i].isupper():
                    score += (ord(strings[0][i]) - 64) + 26
                if strings[0][i].islower():
                    score += (ord(strings[0][i]) - 96)
        strings= []
        dupes = []

print(score)