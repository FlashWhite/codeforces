n, m, a = [int(x) for x in input().split()]
b = n // a
c = m // a
if n % a != 0:
    b += 1
if m % a != 0:
    c += 1
print(b * c)