n = int(input())
l = list(map(int, input().split()))
p = l[0]
curr = 1
mx = 1
for i in range(1,n):
    if l[i] >= p:
        curr += 1
        if curr > mx:
            mx = curr
    else:
        curr = 1
    p = l[i]
print(mx)