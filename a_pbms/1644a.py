t = int(input())
for _ in range(t):
    s = input()
    if s.find("r") < s.find("R") and s.find("g") < s.find("G") and s.find("b") < s.find("B"):
        print("YES")
    else:
        print("NO")