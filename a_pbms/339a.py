d = {"1": 0, "2": 0, "3": 0}
l = input().split("+")
s = ""
for n in l:
    d[n] += 1
for key in d:
    for _ in range(d[key]):
        s += "+{}".format(key)
print(s.strip("+"))