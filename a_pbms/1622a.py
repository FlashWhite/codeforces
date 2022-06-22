t = int(input())
for _ in range(t):
    sides = [int(e) for e in input().split()]
    answer = ""
    for i in range(3):
        ol = sides.copy()
        ol.pop(i)
        if sides[i] == ol[0] + ol[1]:
            answer = "YES"
            break
        if ol[0] == ol[1] and sides[i] % 2 == 0:
            answer = "YES"
            break
    else:
        answer = "NO"
    print(answer)