n = int(input())
input = input().split()
d = {}
i = 1
for x in input:
        d[int(x)] = str(i)
        i += 1
output = []
for i in range(1, n+1):
    output.append(d[i])
print(" ".join(output))