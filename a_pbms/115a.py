n = int(input())
a = [[] for _ in range(n)]
roots = []
for i in range(n):
    x = int(input())
    if x == -1:
        roots.append(i+1)
        continue
    a[x-1].append(i+1)

def height(x):
    if a[x-1] == []:
        return 1
    else:
        children = []
        for child in a[x-1]:
            children.append(height(child))
        return max(children) + 1

l = []
for root in roots:
    l.append(height(root))
print(max(l))

"""
def height(visited, x):
    visited.add(x)
    for child in a[x-1]:
        if child not in visited:
            height(visited, child)
"""
