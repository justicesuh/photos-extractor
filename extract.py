from glob import glob
import sys

if __name__ == '__main__':
    files = glob(sys.argv[1] + '/**', recursive=True)
    for file in files:
        print(file)
