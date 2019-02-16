class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

# from a Terminal (MSDOS)
# >>> import reader
# >>> r = reader.Reader('reader/__init__.py')
# >>> r.read()
# 'from reader.reader import Reader
# \n\nprint(\'reader is being imported\')
# \n\n# C:\\Users\\***\\Desktop\\python-psq
# \\beyondthebasics>python\n#
# Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15)
# [MSC v.1915 64 bit (AMD64)] on win32\n# Type "help",
# "copyright", "credits" or "license" for more information.\n#
# >>> import reader\n#
# >>> type(reader)\n# <class \'module\'>\n#
# >>> reader.__file__\n#
# \'C:\\\\Users\\\\***\\\\Desktop\\\\python-psq\\
# \\beyondthebasics\\\\reader\\\\__init__.py\'\n# >>>\n'
# >>> r.close()


# Alternatively run >
# >>> r = reader.Reader('reader/reader.py')
# >>> r.read()
# "class Reader:\n    def __init__(self, filename):\n
# self.filename = filename\n
# self.f = open(self.filename, 'rt')\n\n
# def close(self):\n        self.f.close()\n\n
# def read(self):\n
# self.f.read()\n\n# from a Terminal (MSDOS)\n#
# >>> r.close()

