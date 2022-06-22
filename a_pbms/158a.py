n, k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
x = l[k-1]
count = 0
for i in range(n):
    if l[i] >= x and l[i] > 0:
        count += 1
print(count)