k, n, w = [int(x) for x in input().split()]
sum = 0
for i in range(1, w+1):
    sum += i * k
print(sum - n if sum > n else 0)