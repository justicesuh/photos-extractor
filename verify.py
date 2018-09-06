import sys
from glob import glob

if __name__ == '__main__':
    files = sum([glob('{}/**/*.{}'.format(sys.argv[1], fmt), recursive=True) for fmt in ['jpeg', 'jpg', 'raw', 'png', 'gif', 'tiff', 'mp4', 'mov']], [])
    print('Found {} files'.format(len(files)))
