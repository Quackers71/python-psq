def ret():
    print("\r")


urls = {'Google': 'http://google.com',
        'Pluralsight': 'http://pluralsight.com',
        'Sixty North': 'http://sixty-north.com',
        'Microsoft': 'http://microsoft.com'}

print(urls['Pluralsight'])

names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
n = dict(names_and_ages)
print("names_and_ages:")
print(names_and_ages)
print("n = dict(names_and_ages):")
print("n =", n)
ret()

phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print("phonetic:")
print(phonetic)
ret()

d = dict(goldenrod=0xDAA520, indigo=0xB0082, seashell=0xFFF5EE)
print("d =", d)
e = d.copy()

print("e = d.copy():")
print("e =", e)

f = dict(e)
print("f = dict(e):")
print("f =", f)
ret()

g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
print("g =", g)
f.update(g)
print("f.update(g):")
print("f =", f)
ret()

stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
print("stocks:")
print(stocks)
stocks.update({'GOOG': 894, 'YHOO': 25})
print("stocks updated:")
print(stocks)
ret()


colors = dict(aquamarine='#7FFFD4', burlywood='#DEB887',
              charreuse='#7FFF00', cornflower='#6495ED',
              firebrick='#B22222', honeydew='#F0FFF0',
              maroon='#B03060', sienna='#A0522D')
for key in colors:
        print("{key} => {value}".format(key=key, value=colors[key]))

ret()
for value in colors.values():
        print(value)

ret()
for key in colors.keys():
        print(key)

ret()

for key, value in colors.items():
        print("{key} => {value}".format(key=key, value=value))

ret()

symbols = dict(usd='\u0024', gbp='\u00a3', nzd='\u0024',
               krw='\u20a9', eur='\u20ac', jpy='\u00a5',
               nok='kr', ils='\u20aa', hhg='Pu')
print(symbols)
print("'nzd' in symbols:", 'nzd' in symbols)
print("'mkd' in symbols:", 'mkd' in symbols)
ret()

z = {'H': 1, 'Tc': 43, 'Xe': 54, 'Un': 137,
     'Rf': 104, 'Fm': 100}
print("z =", z)
del z['Un']
print("del z['Un']:")
print("z =", z)
ret()

m = {'H': [1, 2, 3],
     'He': [3, 4],
     'Li': [6, 7],
     'Be': [7, 9, 10],
     'B': [10, 11],
     'C': [11, 12, 13, 14]}
m['H'] += [4, 5, 6, 7]
print("m['H'] += [4, 5, 6, 7]:")
print("m =", m)
ret()

m['N'] = [13, 14, 15]
print("m['N'] = [13, 14, 15]")
print("m =", m)
ret()

from pprint import pprint as pp
pp(m)
ret()
print("            Pretty printing")
print("Python Standard Library pprint module")
print("Be careful not to rebind the module reference")
print("Knows how to pretty-print all built-in data -")
print("structures, including dict.")
