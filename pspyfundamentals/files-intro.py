import sys

p = sys.getdefaultencoding()
print("\n", p)

f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('What are the roots that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stony rubbish? ')

f.close()

print("\n")
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.read(32))
print(g.read())

g.seek(0)

print("\n")
print(g.readline())
print(g.readline())

g.seek(0)

print("\n")
print(g.readlines())

g.close()

h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['\n\nSon of man,\n',
     'You cannot say, or guess, ',
     'for you know only,\n',
     'A heap of broken images, ',
     'where the sun beats\n'])

h.close()
