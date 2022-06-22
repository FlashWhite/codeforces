t = int(input())
for _ in range(t):
    n = int(input())
    s = str(n)
    output = 9 * (len(s)-1)
    if n >= int(s[0] * len(s)):
        output += int(s[0])
    else:
        output += int(s[0]) - 1
    print(output)
    