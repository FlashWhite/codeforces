n = int(input())
count = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    if b - a >= 2:
        count += 1
print(count)