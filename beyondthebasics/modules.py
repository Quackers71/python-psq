import urllib
import urllib.request
import sys

print(type(urllib))
print(type(urllib.request))
print("\nurllib.__path__ :\n\n", urllib.__path__)

# print(urllib.request.__path__)
# Packages are generally directories
# Modules are generally files

print("\n sys.path :\n\n", sys.path)

print("\nsys.path[0] :", sys.path[0])

print("\nsys.path[-5:] :", sys.path[-5:])

# mkdir not_searched in btb folder
# create the file 'path_test.py'
# - def found():
# -     print('Python found me!')
# from the REPL : (in folder that contains not_searched folder)
# C:\Users\Rob\Desktop\AWS EC2\python-psq\beyondthebasics>python
# Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import path_test.py
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named 'path_test'
# >>> import path_test
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: No module named 'path_test'
# >>> import sys
# >>> sys.path.append('not_searched')
# >>> import path_test
# >>> path_test.found()
# Python found me!
# >>>

# Python Path
# - Environment variable listing paths added to sys.path
# - In 'Git Bash' run - $ export PYTHONPATH=not_searched
# $ python
# >>> import sys
# >>> [p for p in sys.path if 'not_searched' in p]
# >>> import path_test
# >>> path_test.found()
# Python found me!
# >>>
