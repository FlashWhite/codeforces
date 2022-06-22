n = int(input())
sx = 0
sy = 0
sz = 0
for _ in range(n):
    x, y, z = [int(x) for x in input().split()]
    sx += x
    sy += y
    sz += z
if sx == 0 and sy == 0 and sz == 0:
    print("YES")
else:
    print("NO")