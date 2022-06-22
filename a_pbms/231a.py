t = int(input())
d = []
for _ in range(t):
    d.append([int(x) for x in input().split()])
count = 0
for i in range(t):
    if d[i].count(1) >= 2:
        count += 1
print(count)