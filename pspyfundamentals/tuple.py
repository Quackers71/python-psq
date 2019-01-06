# tuples - are immutable sequences of arbitrary objects
# Delimited by parentheses


def ret():
    print("\r")


t = ("Norway", 4.953, 3)
print("t =", t)
print("t[0] =", t[0])
print("t[2] =", t[2])
print("len(t) =", len(t))
ret()

for item in t:
    print(item)

t += (338186.0, 265e9)
print("t + (338186.0, 265e9) =", t)
ret()
t = t * 3
print(t)
ret()
a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))
print(a[2])
print(a[2][1])

h = (391,)  # trailing comma turns int into tuple
print(h)
print(type(h))
ret()

e = ()
print("e = () which is a", type(e))
ret()


def minmax(items):
    return min(items), max(items)


print(minmax([83, 33, 84, 32, 85, 31, 86]))
ret()

lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print(lower)
print(upper)
ret()

# Tuple unpacking works with arbitrarily nested tuples
# (although not with other data structures)

(a, (b, (c, d))) = (4, (3, (2, 1)))

print(a)
print(b)
print(c)
ret()

a = 'jelly'
print("a =", a)
b = 'bean'
print("b =", b)
a, b = b, a
print("a, b = b, a")
print("a =", a)
print("b =", b)
ret()

print(tuple([561, 1105, 1729, 2465]))
ret()
print(tuple("Carmichael"))
ret()
print("5 in tuple list     =", 5 in (3, 5, 17, 257, 65537))

print("5 not in tuple list =", 5 not in (3, 5, 17, 257, 65537))




