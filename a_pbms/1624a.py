t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    maximum = arr[0]
    minimum = arr[0]
    for a in arr:
        if a > maximum:
            maximum = a
        if a < minimum:
            minimum = a
    print(maximum - minimum)
