import os
import uuid

from file import getListFromFileContents

# init
csvFile = 'input\\fileList.csv'
no = 1

csvList = getListFromFileContents(csvFile)

# For each line in the cvs list
for line in csvList:

    # Split the line by a comma into a list
    item = line.split(',')

    # The path is the first two elements
    path = ''.join(item[0:1])

    # The filename is the first element which
    # we split into its prefix and extension
    filename = item[1].split('.')

    # Remake the prefix by joining the filename with periods
    prefix = '.'.join(filename[0:-1])

    # Because there maybe other periods in the
    # filename the extension will always be the last one
    ext = filename[-1]

    # New hex uuid
    hex = uuid.uuid4().hex

    # Set the new paths
    previous = f'{path}{prefix}.{ext}'
    next = f'{path}{hex}_{no}.{ext}'

    # print(f'{previous}...{next}')

    os.rename(previous, next)

    no = no + 1
