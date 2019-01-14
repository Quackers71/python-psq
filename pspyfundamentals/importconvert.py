from exceptional import convert


def ret():
    print("\r")


print(convert("33"))
print(type(convert("33")))
ret()

print("hedgehog", convert("hedgehog"))  # Normally this will produce a Traceback: ValueError

print(convert([4, 5, 6]))
