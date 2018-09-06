from glob import glob
import os
from shutil import copy2
import sys

def copy(src, dst):
    '''
    copy file from src to dst without overwriting existing files
    '''
    filename = src.rsplit(os.sep, 1)[-1]
    if os.path.exists(os.path.join(dst, filename)):
        print('{} exists'.format(filename))
        name, ext = filename.rsplit('.', 1)
        count = 2
        while os.path.exists(os.path.join(dst, '{} ({}).{}'.format(name, count, ext))):
            count += 1
        copy2(src, os.path.join(dst, '{} ({}).{}'.format(name, count, ext)))
    else:
        copy2(src, dst)

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
        copy(file, dst)
