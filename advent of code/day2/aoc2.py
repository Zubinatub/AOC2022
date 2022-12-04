file1 = open('input.txt', 'r')
Lines = file1.readlines()
  
score = 0

for line in Lines:
    currentHand = line.strip()
    
    if (currentHand == 'A X'):
        score += 3
        
    if (currentHand == 'B Y'):
        score += 5

    if (currentHand == 'C Z'):
        score += 7
    
    if (currentHand == 'A Y'):
        score += 4
        
    if (currentHand == 'A Z'):
        score += 8
        
    if (currentHand == 'B X'):
        score += 1
        
    if (currentHand == 'B Z'):
        score += 9
        
    if (currentHand == 'C X'):
        score += 2
        
    if (currentHand == 'C Y'):
        score += 6
        
print('score = ', score)