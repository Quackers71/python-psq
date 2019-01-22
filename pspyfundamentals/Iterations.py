

def ret():
    print("\r")


iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) < produces a Traceback StopIteration Error
ret()


def first(iterable2):
    iterator2 = iter(iterable2)
    try:
        return next(iterator2)
    except StopIteration:
        raise ValueError("iterable is empty")


print(first(["1st", "2nd", "3rd"]))
print(first(["1st", "2nd", "3rd"]))
# print(first(set())) < produces a ValueError: iterable is empty

