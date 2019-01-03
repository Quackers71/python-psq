print("Objects - Argument Passing")
print("\r")

m = [9, 15, 24]
print("m = ", m)


def modify(k):
    k.append(39)
    print("The number", k[-1], "has been appended to the list")
    print("k = ", k)

modify(m)

print("m = ", m)
print("\r")

f = [14, 23, 37]
print("f = ", f)

print("function replace(g) is defined as 'g = [17, 28, 45]'")


def replace(g):
    g = [17, 28, 45]
    print("g = ", g)


print("replace(f) *function called")
replace(f)
print("\r")

print("Replace contents (f) example")


def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g = ", g)


print("f = ", f)

print("replace_contents(f) *function called")
replace_contents(f)

print("f = ", f)

print("\r")
print("Pass By Object Reference")
print("The value of the reference is copied, not the value of the object")
print("\r")


def f(d):
    return d


print("f(d) - return d *function defined")
c = [6, 10, 16]
print("c = ", c)
e = f(c)
print("e = f(c) *called")
print("e = ", e)
print("c is e = ", c is e)

