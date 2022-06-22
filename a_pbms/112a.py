a = input().lower()
b = input().lower()
for i in range(len(a)):
    c = ord(a[i])
    d = ord(b[i])
    if c < d:
        print("-1")
        break
    if d < c:
        print("1")
        break
else:
    print("0")
