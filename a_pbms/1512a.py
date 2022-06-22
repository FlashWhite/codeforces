t = int(input())
for _ in range(t):
    n = int(input())
    l = input().split()
    similar = ""
    if l[0] == l[1] or l[0] == l[2]:
        similar = l[0]
    elif l[1] == l[2]:
        similar = l[1]
    for i in range(n):
        if l[i] != similar:
            print(i+1)
            break