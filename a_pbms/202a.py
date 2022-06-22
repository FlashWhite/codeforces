s = input()
m = ""
mi = 0
n = len(s)
for i in range(n):
    if s[i] > m:
        m = s[i]
        mi = i
count = 1
for j in range(mi+1, n):
    if s[j] == m:
        count += 1
print(m * count)