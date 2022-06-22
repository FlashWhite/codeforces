from collections import defaultdict

n = int(input())
dh = defaultdict(int)
da = defaultdict(int)
s = set()
for _ in range(n):
    h, a = map(int, input().split())
    dh[h] += 1
    da[a] += 1
    s.add(h)
    s.add(a)
total = 0
for i in s:
    total += dh[i] * da[i]
print(total)
