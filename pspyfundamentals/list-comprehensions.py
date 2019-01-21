from math import factorial


def ret():
    print("\r")


words = "Why sometimes I have believed as many as six " \
        "impossible things before breakfast".split()

print(words)

print([len(word) for word in words])
# [expr(item) for item in iterable]

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)
ret()

f = [len(str(factorial(x))) for x in range(20)]
print("f =", f)
print("type(f) =", type(f))