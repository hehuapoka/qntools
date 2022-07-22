import maya.cmds as cmds


def checkRootHierarchy():
    #检查模型的His
    def checkRenderChild(s:str):
        ak = ['main','cloth','hair']
        renders:str = cmds.listRelatives(s,children=True,f=True)
        for i in renders:
            if i.split("|")[-1] not in ak:
                return False
        return True
    def checkGeoChild(s:str):
        geos = cmds.listRelatives(s,children=True,f=True)
        for i in geos:
            if i == "|root|geo|proxy":
                return checkRenderChild(i)
            elif i == "|root|geo|render":
                return checkRenderChild(i)
            else:
                return False
    def checkSimProxyChild(s:str):
        return True
    def checkSimClothChild(s:str):
        return True




    def checkRootChild():
        roots = cmds.listRelatives('|root',children=True,f=True)
        for i in roots:
            if i == "|root|geo":
                return checkGeoChild(i)
            elif i == "|root|simproxy":
                return checkSimProxyChild(i)
            elif i == "|root|simcloth":
                return checkSimClothChild(i)
            else:
                return False


    default_roots =['persp', 'top', 'front', 'side', 'root','bottom','left','back']
    for i in cmds.ls(assemblies=True):
        if i not in default_roots:
            return False
    return checkRootChild()
