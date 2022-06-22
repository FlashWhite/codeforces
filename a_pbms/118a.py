s = input()
l = []
for c in s:
    if c not in "aAeEiIoOuUyY":
        l.append("." + c.lower())
print("".join(l))
