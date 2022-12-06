file1 = open('input.txt', 'r')
signal = file1.read().rstrip()

start = 0
#changed end from 4 to 14 for part 2
end = 14

temp = signal[start:end]
while not (len(set(temp)) == len(temp)):
    start += 1
    end += 1
    temp = signal[start:end]
    
print(start, end)
print(temp)