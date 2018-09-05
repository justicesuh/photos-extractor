from glob import glob
import os
import sys
from shutil import copy2

def create_folders(*folders):
    '''
    create folders if they don't already exist
    '''
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

if __name__ == '__main__':
    src = sys.argv[1]
    dst = sys.argv[2]
    photobooth = '{}/PhotoBooth'.format(dst)
    library = '{}/Library'.format(dst)

    create_folders(dst, photobooth, library)

    # get all media files
    formats = ['jpeg', 'jpg', 'raw', 'png', 'gif', 'tiff', 'mp4', 'mov']
    files = sum([glob('{}/**/*.{}'.format(src, f), recursive=True) for f in formats], [])

    for file in files:
        # Library media
        if 'photoslibrary' in file:
            file = file[file.index('photoslibrary') + 14:]
        # PhotoBooth media
        elif 'Library' in file:
            copy2(file, photobooth)
