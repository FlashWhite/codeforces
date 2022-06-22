n = int(input())
l = [0 for _ in range(n)]
#print(l)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(1, a[0]+1):
    l[a[i]-1] = 1
#print(l)
for j in range(1, b[0]+1):
    l[b[j]-1] = 1
#print(l)
for k in range(n):
    if l[k] == 0:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")