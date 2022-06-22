n, q = map(int, input().split())
p = list(map(int, input().split()))
p = sorted(p, reverse=True)
#print(p)
for _ in range(q):
    x, y = map(int, input().split())
    sum = 0
    for i in range(x - y, x):
        sum += p[i]
    print(sum)