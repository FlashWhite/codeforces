s = input()
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        count = 1
    if count >= 7:
        print("YES")
        break
else:
    print("NO")
