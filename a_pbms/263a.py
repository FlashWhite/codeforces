l = []
for _ in range(5):
    l.append([int(x) for x in input().split()])
for i in range(5):
    for j in range(5):
        if l[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
            break
