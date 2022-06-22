n = int(input())
l = list(map(int, input().split()))
min = 101 
min_i = 0
max = 0
max_i = 0
for i in range(n):
    if l[i] <= min:
        min = l[i]
        min_i = i
    if l[i] > max:
        max = l[i]
        max_i = i
output = n - 1 - min_i + max_i
if min_i < max_i:
    output -= 1
print(output)
