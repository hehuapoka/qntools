import os
def getLastOpen():
    try:
        with open("temp.conf") as pf:
            return os.path.dirname(pf.read())
    except:
        return None
def saveCurrentDir(dir:str):
    try:
        with open("temp.conf","w+") as pf:
            pf.write(os.path.dirname(dir))
        return True
    except:
        return False