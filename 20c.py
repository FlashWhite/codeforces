n, m = map(int, input().split())
g = {}
for i in range(1, n+1):
    g[i] = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a] = (b, c)
    g[b] = (a, c)
    