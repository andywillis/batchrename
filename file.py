import os


# `createFile`
#
# Create a new file
def createFile(filePath):

    with open(filePath, 'a+') as myfile:
        myfile.close()


# `getListFromFileContents`
#
# Create an empty file if it doesn't exist, and return
# an empty array, or read the lines of the file if it does
# exist, and return a filled array
def getListFromFileContents(filePath):

    list = []

    if os.path.isfile(filePath) is False:

        createFile(filePath)

    else:

        file = open(filePath, 'r')
        line = file.readline()

        while line:

            list.append(line.rstrip('\n'))
            line = file.readline()

        file.close()

    return list
