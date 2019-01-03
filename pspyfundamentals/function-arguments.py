# Function Arguments in Detail
import time


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Norwegian Blue")
print("\r")
banner("Sun, Moon and Stars", "*")
print("\r")
banner("Sun, Moon and Start", border="@")
print("\r")
banner(border=".", message="Hello from Earth")
print("\r")

print(time.ctime())
print("\r")


def show_default(arg=time.ctime()):
    print(arg)


show_default()
# time.sleep(0.2)
show_default()
# time.sleep(0.2)
show_default()
time.sleep(0.5)

print("\r")
print("Default Argument Evalution")
print("\r")
print("Default argument values are evaluated when 'def' is evaluated")
print("They can be modified like any other object")
print("\r")


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ['bacon', 'eggs']
print("breakfast = ", breakfast)
print("add_spam(breakfast) = ", add_spam(breakfast))
print("\r")

lunch = ['baked beans']
print("lunch = ", lunch)
print("add_spam(lunch) = ", add_spam(lunch))
print("\r")

print("add_spam()", add_spam())
print("add_spam()", add_spam())
print("add_spam()", add_spam())
print("add_spam()", add_spam())
print("\r")

# Use imutable objects - integers or strings as default values i.e. use the 'None' object


def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


print("Now using an imutable object")
print("add_spam()", add_spam())
print("add_spam()", add_spam())
print("add_spam()", add_spam())
print("add_spam()", add_spam())
