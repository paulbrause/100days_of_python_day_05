heights = input().split()

avg = 0
sum = 0

for height in heights:
    avg += int(height)
    sum += 1
    
avg = avg/sum

print(avg)