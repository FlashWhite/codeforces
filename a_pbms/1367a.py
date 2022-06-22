t = int(input())
for _ in range(t):
    s = input()
    middle = ""
    for i in range(len(s[1:len(s)-1])//2):
        middle += s[i * 2 + 1]
    print(s[0] + middle + s[-1])
