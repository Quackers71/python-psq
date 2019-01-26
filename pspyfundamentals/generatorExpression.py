def ret():
    print("\r")


million_squares = (x*x for x in range(1, 100001))
print(million_squares)
ret()

print(list(million_squares))
print(list(million_squares))
ret()

a = sum(x*x for x in range(1, 10000001))
print(sum)
print(a)
ret()

# NameError: name 'is_prime' is not defined
# b = sum(x for x in range(1001) if is_prime(x))
# print(b)
