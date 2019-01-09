def ret():
    print("\r")


for i in range(5):
    print(i)
ret()

print(range(5))
ret()

print(range(5, 10))
ret()

print("list(range(10, 15) =", list(range(10, 15)))
ret()

print("Constructor          Argument            Result")
print("range(5)             stop                0, 1, 2, 3, 4")
print(list(range(5)))
ret()

print("Constructor          Argument            Result")
print("range(5, 10)         start, stop         5, 6, 7, 8, 9")
print(list(range(5, 10)))
ret()

print("Constructor          Argument            Result")
print("range(10, 20, 2)     start, stop, step   10, 12, 14, 16, 18")
print(list(range(10, 20, 2)))
ret()

# Un-Pythonic - Avoid range() for iterating over lists
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])

ret()

# Prefered - direct iteration over iterable objects, such as lists
for v in s:
    print(v)

ret()

t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p)

ret()

for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))

