i = int(input())
s = ["I", "hate", "it"]
a = "love"
if i != 1:
    for _ in range(1, i):
        s.insert(-1, "that")
        s.insert(-1, "I")
        s. insert(-1, a)
        if a == "love":
            a = "hate"
        else:
            a = "love"
print(" ".join(s))