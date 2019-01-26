from itertools import islice, count


def ret():
    print("\r")


# islice(all_primes, 1000)

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousand_primes)
# print(list(thousand_primes))

a = sum(islice((x for x in count() if is_prime(x)), 1000))
print(a)
