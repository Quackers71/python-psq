# Objects
print("Objects - Introduction")
print("\r")

print("Imutable Objects")
x = 1000
print("x is ", x)
x = 500
print("x is ", x)
y = x
print("y = x")
x = 3000
print("assigned x to equal 3000")
print("x is ", x)
print("y is ", y)

a = 496
print("a - id:", id(a), " and value is ", a)
b = 1729
print("b - id:", id(b), " and value is ", b)

print("b = a")
b = a
print("id(a) == id(b) is ", id(a) == id(b))

print("a is b = ", a is b)
print("a is None = ", a is None)
print("\r")

# Augmented Assignment Operator
print("Augmented Assignment Operator")
t = 5
print("t = ", t)
print("t - id:", id(t))
t += 2
print("t += 2")
print("t - id:", id(t))
print("\r")

# mutable objects - lists
print("Mutable Objects - lists")
r = [2, 4, 6]
print("r = ", r)
print("s = r")
s = r
print("s = ", s)
s[1] = 17
print("s[1] = 17")
print("s = ", s)
print("s is r = ", s is r)
print("r id:", id(r))
print("s id:", id(s))
print("\r")

p = [4, 7, 11]
print("p = ", p)
q = [4, 7, 11]
print("q = ", q)
print("p == q = ", p == q)
print("p is q = ", p is q)
print("p == p = ", p == p)
print("\r")

print("Value equality vs Identity")
print("\r")
print('Value - equivalent "contents"')
print("Identity - same object")
print("\r")
print("Value comparison can be controlled programatically")
print("\r")

