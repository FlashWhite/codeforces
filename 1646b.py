t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    left = l[0] + l[1]
    right = l[n-1]
    output = "NO"
    for i in range(n//2):
        if left < right:
            output = "YES"
            break
        left += l[2 + i]
        right += l[n - 2 - i]
    print(output)