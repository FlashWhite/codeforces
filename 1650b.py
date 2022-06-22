t = int(input())
for _ in range(t):
    l, r, a = map(int, input().split())
    output = r // a + r % a
    val = (r // a) * a - 1
    if l <= val <= r:
        val2 = (r // a - 1) + (a - 1)
        if val2 > output:
            output = val2
    print(output)