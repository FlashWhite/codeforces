n, h = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
total = 0
for x in l:
    if x > h:
        total += 2
    else:
        total += 1
print(total)