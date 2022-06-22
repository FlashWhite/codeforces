t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    div = n // x
    if div * x + y > n:
        div -= 1
    print(div * x + y)