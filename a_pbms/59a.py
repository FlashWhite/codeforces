import string
s = input()
lower_count = 0
upper_count = 0
for c in s:
    if c in string.ascii_lowercase:
        lower_count += 1
    elif c in string.ascii_uppercase:
        upper_count += 1
if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())