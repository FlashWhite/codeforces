t = int(input())
for _ in range(t):
    n = int(input())
    l = input().split()
    first = -1
    last = -1
    for i in range(n):
        if l[i] == "0":
            first = i
            break
    if first == -1:
        print(0)
    else:
        j = n-1
        while j > first:
            if l[j] == "0":
                last = j
                break
            j -= 1
        if last == -1:
            print(2)
        else:
            print(last - first + 2)