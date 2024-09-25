import os


def getPackagePath(filename):
    return  os.path.join(os.path.dirname(__file__), '../'+filename)