t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    # changing a, observe b c gap
    d = c - b
    if b - d >= a and (b - d) % a == 0:
        if b - d != 0:
            print("YES")
            continue
    # changing b, observe a c gap
    if (c - a) % 2 == 0:
        d = (c - a) // 2 
        if a + d >= b and (a + d) % b == 0 and a + d != 0:
            print("YES")
            continue 
    # changing c, observe a b gap
    d = b - a
    if b + d >= c and (b + d) % c == 0:
        if b + d != 0:
            print("YES")
            continue
    print("NO")

