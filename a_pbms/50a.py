a, b = [int(x) for x in input().split()]
if a > 1 or b > 1:
    if a % 2 == 0 and b % 2 == 0:
        print(a // 2 * b)
    elif a % 2 != 0 and b % 2 != 0:
        print(a // 2 * b + b // 2)
    elif a % 2 == 0 and b % 2 != 0:
        print(a // 2 * b)
    elif a % 2 != 0 and b % 2 == 0:
        print(b // 2 * a)
else:
    print("0")