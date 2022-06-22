t = int(input())
for _ in range(t):
    a, b, c, x, y = map(int, input().split())
    dog = x - a if x - a >= 0 else 0
    #print(dog)
    cat = y - b if y - b >= 0 else 0
    #print(cat)
    if dog + cat <= c:
        print("YES")
    else:
        print("NO")