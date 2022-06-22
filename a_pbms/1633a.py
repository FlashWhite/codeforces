l = [7 * i for i in range(2, 143)]
t = int(input())
for _ in range(t):
    n = int(input())

    if n % 7 == 0:
        lowest = str(n).lstrip("0")
    else:
        least_changes = 3
        lowest = 0
        for j in l:
            count = 0
            if n // 100 != j // 100:
                count += 1
            if n // 10 != j // 10:
                count += 1
            if n % 10 != j % 10:
                count += 1
            if count < least_changes:
                least_changes = count
                lowest = j
            if least_changes == 1:
                break
    print(lowest)