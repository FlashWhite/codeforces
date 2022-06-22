t = int(input())
for _ in range(t):
    odds = 0
    evens = 0
    wrong_evens = 0
    wrong_odds = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        if l[i] % 2 == 0:
            evens += 1
            if i % 2 != 0:
                wrong_evens += 1
        else:
            odds += 1
            if i % 2 == 0:
                wrong_odds += 1
    if wrong_evens == 0 and wrong_odds == 0:
        print(0)
    elif n % 2 == 0:
        if evens == odds and wrong_evens == wrong_odds:
            print(wrong_evens)
        else:
            print(-1)
    else:
        if evens == odds + 1 and wrong_evens == wrong_odds:
            print(wrong_evens)
        else:
            print(-1)