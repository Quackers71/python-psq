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
ret()

# Prt2
# set algebra
print("Prt2")
ret()

blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}  # Hydrogen Cyanide (HCN)
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}  # Phenylthiocarbamide (PTC)
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

print("blue_eyes.union(blond_hair):")
print(blue_eyes.union(blond_hair))
ret()
print("blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes):", blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
ret()
print("blue_eyes.intersection(blond_hair):")
print(blue_eyes.intersection(blond_hair))
ret()
print("blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes):", blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))
ret()

print("blond_hair.difference(blue_eyes):")
print(blond_hair.difference(blue_eyes))
ret()

print("blond_hair.symmetric_difference(blue_eyes):")
print(blond_hair.symmetric_difference(blue_eyes))

print("blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair):", blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))
ret()

print("smell_hcn.issubset(blond_hair):", smell_hcn.issubset(blond_hair))
print("taste_ptc.issuperset(smell_hcn):", taste_ptc.issuperset(smell_hcn))
print("a_blood.isdisjoint(o_blood):", a_blood.isdisjoint(o_blood))


