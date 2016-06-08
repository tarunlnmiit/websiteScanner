import os

def createDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def writeFile(path, data):
    fhand = open(path, 'w')
    fhand.write(data)
    fhand.close()
