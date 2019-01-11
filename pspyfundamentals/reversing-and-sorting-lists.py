def ret():
    print("\r")


g = [1, 11, 21, 1211, 112111]
print("g =", g)

g.reverse()
print("g.reverse():")
print(g)
ret()

d = [5, 17, 41, 29, 71, 149, 3299, 7, 13, 67]
print("d =", d)

d.sort()
print("d.sort():")
print("d =", d)

d.sort(reverse=True)
print("d.sort(reverse=True):")
print("d =", d)
ret()

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print("h =", h)

h.sort(key=len)
print("h.sort(key=len):")
print(h)

print("' '.join(h):")
print(' '.join(h))
ret()

x = [4, 9, 2, 1]
print("x =", x)
y = sorted(x)
print("y = sorted(x):")
print("y =", y)
print("x =", x)

p = [9, 3, 1, 0]
print("p =", p)
q = reversed(p)
print("q = reversed(p):")
print("q =", q)
print("list(q):")
print(list(q))
