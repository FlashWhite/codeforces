n = int(input())
current = 0
max = 0
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    current += (b - a)
    if current > max:
        max = current
print(max)