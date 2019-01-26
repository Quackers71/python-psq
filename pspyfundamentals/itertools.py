from itertools import islice, count, chain
# Most of the below code is better placed
# in the Python console via CMD
# without the 'print()' statements


def ret():
    print("\r")


# islice(all_primes, 1000)

# thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
# print(thousand_primes)
# print(list(thousand_primes))

# a = sum(islice((x for x in count() if is_prime(x)), 1000))
# print(a)

print(any([False, False, True]))
ret()
print(all([False, False, True]))
ret()
# print(any(is_prime(x) for x in range(1328, 1361)))

print(all(name == name.title() for name in ['London', 'New York', 'Sydney']))

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

for item in zip(sunday, monday):
    print(item)

ret()

for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

ret()
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for temps in zip(sunday, monday, tuesday):
    print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(
           min(temps), max(temps), sum(temps) / len(temps)))

ret()
temperatures = chain(sunday, monday, tuesday)

print(all(t > 0 for t in temperatures))

for x in (p for p in lucas() if is_prime(p)):
    print(x)
