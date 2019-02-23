from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']

# from module import *
# The __all__ attribute should be a list of strings
# containing names available in the module.

# >>> from reader.compressed import *
# reader is being imported
# >>> locals()
# {'__name__': '__main__', '__doc__': None, '__package__':
# None, '__loader__': <class '_frozen_
# importlib.BuiltinImporter'>, '__spec__': None,
# '__annotations__': {}, '__builtins__':
# <module 'builtins' (built-in)>, 'bz2_opener':
# <function open at 0x00B79ED0>, 'gzip_opener':
# <function open at 0x02856D20>}

# >>> bz2_opener
# <function open at 0x00B79ED0>

# >>> gzip_opener
# <function open at 0x02856D20>
# >>>
