n = int(input())
prev = int(input())
count = 1
for _ in range(n-1):
    current = int(input())
    if prev != current:
        count += 1
    prev = current
print(count)

"""
n = int(input())
count = 1
l = []
for _ in range(n):
    l.append(input())
for i in range(1,n):
    if l[i-1] != l[i]:
        count += 1
print(count)


n = int(input())
count = 1
l = [input()]
for i in range(n-1):
    l.append(input())
    if l[i-1] != l[i]:
        count += 1
print(count)
"""

"""
n = int(input())
count = 1
prev = input()
for _ in range(n-1):
    x = input()
    if prev != x:
        count += 1
        prev = x
print(count)
"""