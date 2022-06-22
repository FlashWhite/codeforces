t = int(input())
for _ in range(t):
    r, g, b, w = map(int, input().split())
    e = 0
    o = 0
    toggle = True
    if w % 2 == 0:
        e += 1
    else: 
        o += 1
    for i in [r, g, b]:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
        if i == 0:
            toggle = False
    
    if e == 4 or (e == 3 and o == 1):
        print("Yes")
    elif toggle and (o == 4 or (o == 3 and e ==1)):
        print("Yes")
    else:
        print("No")