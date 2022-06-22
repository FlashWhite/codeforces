n = int(input())
s = input().split()
d = {}
for i in range(1,n+1):
    d[i] = int(s[i-1])
for u in range(1, n+1):
    x = d[u]
    y = d[x]
    if d[y] == u:
        print("YES")
        break

else:
    print("NO")
