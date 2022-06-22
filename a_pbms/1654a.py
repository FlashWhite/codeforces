t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l, reverse=True)
    print(l[0] + l[1])