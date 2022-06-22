s = input()
l = s.split("WUB")
output = ""
for x in l:
    if x != "":
        output += x + " "
print(output[:-1])