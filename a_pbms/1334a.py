t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 0
    bool = True
    for i in range(n):
        x, y = map(int, input().split())
        if bool:
            # decrease / increase in clears > increase in plays
            if x < a or y < b or y - b > x - a:
                bool = False
            a = x
            b = y
    print("YES" if bool else "NO")