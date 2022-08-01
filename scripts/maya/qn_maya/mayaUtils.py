import maya.cmds as cmds
def createModelHierarchy():
    cmds.group(em=True,n="main")
    cmds.group(em=True,n="cloth")
    cmds.group(em=True,n="hair")
    cmds.group(em=True,n="render")
    cmds.parent("|main","render")
    cmds.parent("|cloth","render")
    cmds.parent("|hair","render")

    cmds.group(em=True,n="main")
    cmds.group(em=True,n="cloth")
    cmds.group(em=True,n="hair")
    cmds.group(em=True,n="proxy")
    cmds.parent("|main","proxy")
    cmds.parent("|cloth","proxy")
    cmds.parent("|hair","proxy")

    cmds.group(em=True,n="geo")
    cmds.parent("|render","geo")
    cmds.parent("|proxy","geo")

    cmds.group(em=True,n="simproxy")
    cmds.group(em=True,n="clothproxy")

    cmds.group(em=True,n="root")
    cmds.parent("|geo","root")
    cmds.parent("|simproxy","root")
    cmds.parent("|clothproxy","root")

    def lockTransform(path):
        cmds.setAttr("{}.tx".format(path),lock=True)
        cmds.setAttr("{}.ty".format(path),lock=True)
        cmds.setAttr("{}.tz".format(path),lock=True)
        
        cmds.setAttr("{}.rx".format(path),lock=True)
        cmds.setAttr("{}.ry".format(path),lock=True)
        cmds.setAttr("{}.rz".format(path),lock=True)
        
        cmds.setAttr("{}.sx".format(path),lock=True)
        cmds.setAttr("{}.sy".format(path),lock=True)
        cmds.setAttr("{}.sz".format(path),lock=True)
    lockTransform("|root")

    lockTransform("|root|geo")
    lockTransform("|root|simproxy")
    lockTransform("|root|clothproxy")

    lockTransform("|root|geo|render")
    lockTransform("|root|geo|proxy")
        
    lockTransform("|root|geo|proxy|main")
    lockTransform("|root|geo|proxy|cloth")
    lockTransform("|root|geo|proxy|hair")

    lockTransform("|root|geo|render|main")
    lockTransform("|root|geo|render|cloth")
    lockTransform("|root|geo|render|hair")


def usdExportCmd(outpath,stratframe,endframe,colorsets,uvsets,normals,shaders):
    root_his=cmds.ls(sl=True,long=True)[0]
    
    subdiv="catmullClark"
    mats = "none"
    if shaders:
        mats = "useRegistry"
    if normals:
        subdiv = "none"
    cmds.mayaUSDExport(
                    file=outpath,
                    exportColorSets = colorsets,
                    exportBlendShapes = False,
                    exportUVs=uvsets,
                    shadingMode=mats,
                    defaultMeshScheme= subdiv,
                    staticSingleSample=True,
                    selection=True,
                    frameRange=[stratframe,endframe],
                    stripNamespaces=1,
                    renderableOnly=False,
                    exportRoots=root_his   
                   )
                   
def usdExportThread(data):
    usdExportCmd(data['path'],data['sf'],data['ef'],data['c'],data['uv'],data['n'],data['mat'])

