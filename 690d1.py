r, c = map(int, input().split())
for i in range(r):
    v = input()
    if i == r - 1:
        v = v.lstrip(".")
        v = v.rstrip(".")
        l = len(v)
        count = 0
        b = True
        for j in range(l):
            if v[j] == "." and b:
                count += 1
                b = False
            elif v[j] == "B" and not b:
                b = True
print(count + 1)

