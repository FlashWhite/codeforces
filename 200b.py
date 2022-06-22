n = int(input())
p = [int(x) for x in input().split()]
sum = 0
for i in p:
    sum += i
print("%.12f" % (sum / n))