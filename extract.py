from glob import glob
import os
import sys
from shutil import copy2

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]

    if not os.path.exists(dst):
        os.makedirs(dst)

    files = []
    folders = ['Masters', 'Originals', 'Pictures']
    formats = ['jpeg', 'jpg', 'raw', 'png', 'gif', 'tiff', 'mp4', 'mov']
    for folder in folders:
        for fmt in formats:
            print('Searching {} for *.{}'.format(folder, fmt))
            files.extend(glob('{}/**/{}/**/*.{}'.format(src, folder, fmt), recursive=True))
    num = len(files)
    print()
    print('Found {} items'.format(num))
    print()

    for i, file in enumerate(files, 1):
        print('Copying item {} of {}'.format(i, num))
        copy2(file, dst)
