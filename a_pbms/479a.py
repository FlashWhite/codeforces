a = int(input())
b = int(input())
c = int(input())
m = 0
l = [a+b+c, a+b*c, (a+b)*c, a*b*c, a*(b+c), a*b+c]
for n in l:
    if n > m:
        m = n
print(m)
