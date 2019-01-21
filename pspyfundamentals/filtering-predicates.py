from math import sqrt
from pprint import pprint as pp


def ret():
    print("\r")


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


print([x for x in range(101) if is_prime(x)])
ret()
# [expr(item) for item in iterable if predicate(item)]
#                           above  {optional filtering clause)

# Filtering works with:
# - list comprehensions
# - set comprehensions
# - dictionary comprehensions

prime_square_divisors = {x*x:(1, x, x*x) for x in range(101)
                         if is_prime(x)}
pp(prime_square_divisors)

# Moment of Zen
# Simple is better than complex
# - Code is written once
# - But read over and over
# - Fewer is clearer
