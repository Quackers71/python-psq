def ret():
    print("\r")


s = "show how to index into sequences".split()

print("s      =", s)
print("s[0:6] =", s[0:6], " zero based indexing")
print("s[-6:] =", s[-6:], " negative based indexing")
ret()

print("s[4] =", s[4])
ret()

print("s[-5]", s[-5])
ret()

print("slice = seq[start:stop]")
print("s[1:4] =", s[1:4])
ret()

print("s[1:-1 =", s[1:-1])
ret()

print("s[:3] =", s[:3])
ret()

print("s[3:] =", s[3:])
ret()

full_slice = s[:]
print("full_slice = s: ", full_slice)
ret()
print("full_slice is s:", full_slice is s)
print("full_slice == s:", full_slice == s)
ret()

u = s.copy()
print("u = s.copy: u =", u)
ret()

v = list(s)
print("v = list(s): v =", v)
ret()

print("************************************")
print("         list")
print("     copying lists")
ret()
print("Full slice:          t = seq[]")
print("copy() method:       u  = seq.copy()")
print("list()constructor:   v = list(seq)")

