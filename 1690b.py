t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] - b[i] for i in range(n)]
    #print(c)
    m = 0
    ans = 1
    for v in c:
        if v < 0:
            #print("encountered negative difference, setting to NO")
            ans = 0
            break
        elif v > m:
            m = v
    if ans:
        for i in range(n):
            if c[i] != m and b[i] != 0:
                #print("encountered smaller difference than max and b isn't 0, setting to NO")
                ans = 0
                break
    print("YES" if ans else "NO")