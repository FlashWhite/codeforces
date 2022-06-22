n = int(input())
l = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    minimum = l[0]
    maximum = l[0]
    total = 0
    for i in range(1, n):
        if l[i] > maximum:
            maximum = l[i]
            total += 1
        elif l[i] < minimum:
            minimum = l[i]
            total += 1
    print(total)