n = int(input())
l = [int(x) for x in input().split()]
for x in l:
    if x == 1:
        print("HARD")
        break
else:
    print("EASY")
