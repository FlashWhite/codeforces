t = int(input())
for _ in range(t):
    s = input()
    l = len(s)
    if l % 2 == 0:
        if s[:l//2] == s[l//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")