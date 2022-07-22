import maya.cmds as cmds

def cleanUnknown():
    for i in cmds.ls(type="unknown"):
        cmds.lockNode(i,l=False,lu=False)
        cmds.delete(i)