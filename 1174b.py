n = int(input())
a = list(map(int, input().split()))

e = False
o = False
b = False
for x in a:
    if x % 2 == 0:
        e = True
    else:
        o = True
    if e and o:
        b = True
        break
if b:
    a = sorted(a)
output = list(map(str, a))
print(" ".join(output))