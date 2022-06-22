t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = [s[0]]
    cur = s[0]
    for i in range(1, len(s)):
        c = s[i]
        if cur != c:
            if c in l:
                print("NO")
                break
            else:
                cur = c
                l.append(c)
    else:
        print("YES")