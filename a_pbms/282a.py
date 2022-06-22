n = int(input())
l = [0, 0]
for _ in range(n):
    if input()[1] == "+":
        l[0] += 1
    else:
        l[1] += 1
print(l[0] - l[1])