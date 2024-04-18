heights = input().split()

max = 0

for height in heights:
    if int(height) > max:
        max = int(height)
        
print (max)