import math


def ret():
    print("\r")


print("str")
ret()

gogoch = "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
print(gogoch, "has", len(gogoch), "characters")
ret()

print("New" + "found" + "land")

s = "New"
s += "found"
s += "land"
print(s)
ret()

# Using 'join'
colours = ';'.join(['#45ff23','#2321fa', '#1298a3', '#a32312'])
print("joining the colours:\n", colours)
ret()
print("using colour.split(';')\n", colours.split(';'))
ret()

print(''.join(['high', 'way', 'man']))
ret()

parti = "unforgettable"
print(parti.partition("forget"))
ret()

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
ret()

origin, _, destination = "Seattle-Boston".partition('-')
print(origin)
print(destination)
ret()

print("The age of {0} is {1}".format('Jim', 32))
ret()

print("The age of {0} is {1}. {0}'s Birthday is on {2}".format('Fred', 24, 'October 31'))
ret()

print("Reticulating spline {} of {}.".format(4, 23))
ret()

print("Current position {latitude} {longitude}".format(latitude="60N",
                                                       longitude="5E"))
ret()

pos = (65.2, 23.1, 82.2)
print("Galactic position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))
ret()

print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
ret()
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

# Other string Methods can be learnt about using help(str) from CMD>Python

