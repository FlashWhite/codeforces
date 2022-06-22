t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    right = n-1
    left = 0
    check = True
    for i in range(n):
        if s[i] == "0" and check:
            right = i
            check = False
        if s[i] == "1":
            left = i
    print(right-left+1)