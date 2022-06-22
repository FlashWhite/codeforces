tests = int(input())
for i in range(tests):
    test = input()
    answer = ""
    count = 0
    for c in test:
        if c == "N":
            count += 1
        if count > 1:
            answer = "YES"
            break
    if answer == "":
        if count == 0:
            answer = "YES"
        else:
            answer = "NO"
    print(answer)