file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
count2 = 0
splitID = []

for line in Lines:
    string = line.strip()
    ids = string.split(',')
    section1 = ids[0].split("-")
    section2 = ids[1].split("-")

    section1Start = int(section1[0])
    section1End = int(section1[1])
    
    section2Start = int(section2[0])
    section2End = int(section2[1])

    if section1Start <= section2Start and section1End >= section2End:
        count += 1
        count2 += 1
    elif section2Start <= section1Start and section2End >= section1End:
        count += 1
        count2 += 1
    elif section1Start <= section2Start and section1End >= section2Start:
        count2 += 1
    elif section1Start <= section2End and section1End >= section2End:
        count2 += 1
    elif section2Start <= section1Start and section2End >= section1Start:
        count2 += 1
    elif section2Start <= section1End and section2End >= section1End:
        count2 += 1     

#part 1 answer    
print(count)
#part 2 answer
print(count2)