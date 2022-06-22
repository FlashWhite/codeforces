s = input()
h = "hello"
i = 0
for c in s:
    if c == h[i]:
        i += 1
    if i > 4:
        print("YES")
        break
else:
    print("NO")
