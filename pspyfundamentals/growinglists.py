def ret():
    print("\r")


m = [2, 1, 3]
print("m =", m)
n = [4, 7, 11]
print("n =", n)
ret()
k = m + n
print("k = m + n:")
print(k)
ret()

k += [18, 29, 47]
print("k += [18, 29, 47]:")
print(k)
ret()

k.extend([76, 129, 199])
print("k.extend([76, 129, 199]):")
print(k)
ret()
