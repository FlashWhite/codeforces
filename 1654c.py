t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        a = input()
        print("YES")
    else:
        a = list(map(int, input().split()))
        a = sorted(a)
        curr = a[0]
        ans = "YES"
        for i in range(1, n):
            if abs(curr - a[i]) > 1:
                ans = "NO"
                break
            curr = curr + a[i]
        print(ans)