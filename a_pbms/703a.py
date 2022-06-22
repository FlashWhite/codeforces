n = int(input())
mt = 0
ct = 0
for _ in range(n):
    m, c = map(int, input().split())
    if m > c:
        mt += 1
    elif m < c:
        ct += 1
if mt > ct:
    print("Mishka")
elif mt < ct:
    print("Chris")
else:
    print("Friendship is magic!^^")