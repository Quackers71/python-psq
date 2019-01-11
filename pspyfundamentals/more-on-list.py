def ret():
    print("\r")


ret()
w = "the quick brown fox jumps over the lazy dog".split()
print("w =", w)
ret()

i = w.index('fox')
print("i = w.index('fox'):", i)
ret()

# i = w.index('unicorn')
# print("i = w.index('unicorn'):", i)
# ret()
# Produces a value error

print("37 in [1, 78, 9, 37, 34, 53] =", 37 in [1, 78, 9, 37, 34, 53])
print("78 not in [1, 78, 9, 37, 34, 53] =", 78 not in [1, 78, 9, 37, 34, 53])
ret()

u = "jackdaws love my big sphinx of quartz".split()
print(u)
u.remove('jackdaws')
print("u.remove('jackdaws')")
print(u)
ret()

del u[u.index('quartz')]
print("del u[u.index('quartz')]")
print(u)
ret()

# u.remove('pyramid')
# Produces a value error

a = "I accidentally the whole universe".split()
print(a)

a.insert(2, "destroyed")
print(a)

print(' '.join(a))
