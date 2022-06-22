s = input()
t = input()
if len(s) == len(t):
    n = len(s)
    for i in range(n):
        if s[i] != t[n-i-1]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")