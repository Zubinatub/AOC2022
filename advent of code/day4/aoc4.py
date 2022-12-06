file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
count2 = 0

for line in Lines:
    string = line.strip()
    ids = string.split(',')
    one, two = ids[0].split('-')
    three, four = ids[1].split('-')
    
    listOne = set(list(range(int(one), int(two)+1)))
    listTwo = set(list(range(int(three), int(four)+1)))
    
    if listOne.issubset(listTwo) or listTwo.issubset(listOne):
        count += 1
        
    if listOne.intersection(listTwo):
        count2 += 1
    
    print(count)
    print(count2)