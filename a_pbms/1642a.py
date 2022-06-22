t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    total = 0
    if a[1] == b[1] and a[1] != 0:
        total += abs(a[0] - b[0])
    elif a[1] == c[1] and a[1] != 0:
        total += abs(a[0] - c[0])
    elif b[1] == c[1] and b[1] != 0:
        total += abs(b[0] - c[0])
    print(total)