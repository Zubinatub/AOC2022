# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
  
maxCal = 0
tempVal = 0
count = 0
second = 0
third = 0
# Strips the newline character
for line in Lines:
    if line.strip():
        tempVal = tempVal + int(line)
    else:
        if tempVal >= maxCal:
            third = second
            second = maxCal
            maxCal = tempVal
        if tempVal < maxCal and tempVal > second:
            third = second
            second = tempVal
        if tempVal < second and tempVal > third:
            third = tempVal
        tempVal = 0
        print(maxCal, second, third)
    
print("third cal = ", third)
print("second cal = ", second)
print("max cal = ", maxCal)
print(third + second + maxCal)