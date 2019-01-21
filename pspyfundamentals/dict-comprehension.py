from pprint import pprint as pp
import os
import glob


def ret():
    print("\r")

# {'key_expr': 'value_expr' for item in iterable}
country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat',
                      'Sweden': 'Stockholm'}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)
ret()

# Duplicates: later keys overwrite earlier keys
words = ["hi", "hello", "foxtrot", "hotel"]
print({x[0]: x for x in words})

file_sizes = {os.path.realpath(p): os.stat(p).st_size
              for p in glob.glob('*.py')}
pp(file_sizes)
