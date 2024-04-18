target = int(input())

if target > 1000:
    print("Too much to calculate")
else:
    sum = 0
    for number in range(2, target + 1, 2):
        sum += number
    print(sum)