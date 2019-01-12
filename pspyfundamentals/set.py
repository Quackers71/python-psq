def ret():
    print("\r")

ret()
p = {6, 28, 496, 8128, 33550336}
print(p)
print(type(p))

d = {}
print("d = {}:", type(d))

e = set()
print("e = set():", e)
ret()

s = set([2, 4, 16, 64, 4096, 65536, 262144])
print("s =", s)

t = [1, 4, 2, 1, 7, 9, 9]
print("set(t):", set(t))
ret()

for x in {1, 2, 4, 8, 16, 32}:
    print(x)

ret()

q = {2, 9, 6, 4}
print("q =", q)
print("3 not in q:", 3 not in q)
ret()

k = {81, 108}
print("k =", k)
k.add(54)
print("k.add(54):")
print("k =", k)
k.add(12)
print("k.add(12):")
print("k =", k)
k.add(108)  # exists - no affect or error
print("k.add(108): < this exists - therefore no affect or error")
print("k =", k)
k.update([37, 128, 97])
print("k.update([37, 128, 97]}")
print("k =", k)
ret()

k = {128, 97, 37, 12, 108, 81, 54}
print("k =", k)
k.remove(97)
print("k.remove(97):")
print("k =", k)
print("k.remove(98)  # Traceback - KeyError: 98")
k.discard(98)
print("k.discard(98): < doesn't exist - therefore no affect or error")
ret()

print("k =", k)
j = k.copy()
print("j = k.copy():")
print("j =", j)

m = set(j)
print("m = set(j):")
print("m =", m)

