n, l = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
m = 0
for i in range(n-1):
    v = a[i+1] - a[i]
    if v > m:
        m = v
print(max(m/2, a[0], l-a[n-1]))
