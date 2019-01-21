from math import factorial


def ret():
    print("\r")


f = [len(str(factorial(x))) for x in range(20)]
print(f)
print(type(f))
ret()

print({len(str(factorial(x))) for x in range(20)})
# {expr(item) for item in iterable}
