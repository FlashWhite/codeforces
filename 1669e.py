from collections import defaultdict
ak = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

t = int(input())
for _ in range(t):
    count = 0
    d = defaultdict(int)
    n = int(input())
    for i in range(n):
        s = input()
        for c in ak:
            if c != s[0]:
                if d[c + s[1]] > 0:
                    count += d[c + s[1]]
            if c != s[1]:
                if d[s[0] + c] > 0:
                    count += d[s[0] + c]
        d[s] += 1
    print(count)