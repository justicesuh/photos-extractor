from glob import glob
import sys

def get_formats(files):
    '''
    return list of formats present
    '''
    formats = []
    for file in files:
        if file.count('.') == 2:
            ext = file[file.rindex('.') + 1:]
            if ext not in formats:
                formats.append(ext)
    return formats

if __name__ == '__main__':
    files = map(str.lower, glob(sys.argv[1] + '/**', recursive=True))
    formats = get_formats(files)
    for fmt in formats:
        print(fmt)
