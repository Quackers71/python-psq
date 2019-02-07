from urllib.request import urlopen


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


with open('wasteland.txt', mode='rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)

print(wpl)
print(type(real_file))
print("\n")


with urlopen('http://sixty-north.com/c/t.txt') as web_file:
    wpl = words_per_line(web_file)

print(wpl)
print(web_file)
