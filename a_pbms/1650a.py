t = int(input())
for _ in range(t):
    s = input()
    c = input()
    ans = "NO"
    for i in range(len(s)):
        if s[i] == c and i % 2 == 0:
            ans = "YES"
            break
    print(ans)
