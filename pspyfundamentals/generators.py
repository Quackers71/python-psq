

def ret():
    print("\r")


def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
print(g)

print(next(g))
print(next(g))
print(next(g))

# print(next(g))
ret()

for v in gen123():
    print(v)

h = gen123()
i = gen123()

print(h)
ret()
print(i)

print("h is i:", h is i)
print(next(h))
print(next(h))
print(next(i))
ret()


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6


g = gen246()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
