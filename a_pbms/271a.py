y = int(input())
x = y + 1
digits = {x // 1000, x // 100 % 10, x % 100 // 10, x % 10}
while len(digits) != 4:
    x += 1
    digits = {x // 1000, x // 100 % 10, x % 100 // 10, x % 10}
print(x)