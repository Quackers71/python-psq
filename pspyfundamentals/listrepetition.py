def ret():
    print("\r")


c = [21, 37]
d = c * 4
print(c)
print("d = c * 4:", d)
ret()

print("[0] * 9:", [0] * 9)
ret()

print("s = [constant] * size")
ret()

s = [[-1, +1]] * 5
print("s = [[-1, +1]] * 5:")
print(s)
ret()

s[3].append(7)
print("s[3].append(7):")
print(s)
ret()

