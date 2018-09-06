from glob import glob
import os
from shutil import copy2
import sys

def create_folder(folder):
    '''
    create folder if it doesn't exist
    '''
    if not os.path.exists(folder):
        os.makedirs(folder)

def parse_date(path):
    '''
    parse date from filepath
    '''
    parts = path.split(os.sep)
    index = -1
    for i, part in enumerate(parts):
        try:
            int(part)
            index = i
            break
        except ValueError:
            pass
    return None if index == -1 else ''.join(parts[index:index + 3])

def copy(src, dst):
    '''
    copy file from src to dst without overwriting existing files
    '''
    filename = src.rsplit(os.sep, 1)[-1]
    if os.path.exists(os.path.join(dst, filename)):
        name, ext = filename.rsplit('.', 1)
        count = 2
        while os.path.exists(os.path.join(dst, '{}_{}.{}'.format(name, count, ext))):
            count += 1
        copy2(src, os.path.join(dst, '{}_{}.{}'.format(name, count, ext)))
    else:
        copy2(src, dst)

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]

    create_folder(dst)

    files = []
    folders = ['Masters', 'Originals', 'Pictures']
    formats = ['jpeg', 'jpg', 'raw', 'png', 'gif', 'tiff', 'mp4', 'mov']
    for folder in folders:
        for fmt in formats:
            print('Searching {} for *.{}'.format(folder, fmt))
            files.extend(glob('{}/**/{}/**/*.{}'.format(src, folder, fmt), recursive=True))
    num = len(files)
    print()
    print('Found {} files'.format(num))
    print()

    for i, file in enumerate(files, 1):
        print('Copying file {} of {}'.format(i, num))
        date = parse_date(file):
        if date:
            folder = os.path.join(dst, parse_date(file))
            create_folder(folder)
            copy(file, folder)
        else:
            copy(file, dst)
