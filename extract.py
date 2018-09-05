from glob import glob
import sys

if __name__ == '__main__':
    formats = ['jpeg', 'jpg', 'raw', 'png', 'gif', 'tiff', 'mp4', 'mov']
    files = sum([glob(sys.argv[1] + '/**/*.' + f, recursive=True) for f in formats], [])

    folders = []
    for file in files:
        if 'photoslibrary' in file:
            file = file[file.index('photoslibrary') + 14:]
        else:
            file = file[file.index('Library') + 8:]
        folder = file[:file.index('\\')]
        if folder not in folders:
            folders.append(folder)
    for folder in folders:
        print(folder)