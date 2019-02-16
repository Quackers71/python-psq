import gzip
import sys

opener = gzip.open

if __name__ == '__main__':
    f = gzip.open(sys.argv[1], mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()

# from the cmd line
# >>> import reader
# reader is being imported
# >>> import reader.compressed
# >>> import reader.compressed.gzipped
# >>> import reader.compressed.bzipped
# >>>
