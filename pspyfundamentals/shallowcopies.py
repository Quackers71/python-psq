def ret():
    print("\r")


a = [ [1, 2], [3, 4] ]
print("a =", a)
ret()

b = a[:]
print("b =", b)
ret()

print("a is b =", a is b)
ret()

print("a == b is", a == b)
ret()

print(a[0])
print(b[0])
print("a[0] is b[0] =", a[0] is b[0])
ret()

a[0] = [8, 9]
print("a[0] is now:", a[0])

print("b[0] is    :", b[0])
ret()

print("a[1] is    :", a[1])
print("b[1] is    :", b[1])
a[1].append(5)
print("a[1].append(5)")
print("a[1] is now:", a[1])
print("b[1] is now:", b[1])
ret()

print("a is:", a)
print("b is:", b)

