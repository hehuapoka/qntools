import os
import maya.cmds as cmds
import maya.mel as mel


#资产工具

def usdAssetExport_render(dir:str):
    cmds.select("|root")
    mel.eval(f'arnoldExportAss -f "{dir}" -s -boundingBox -mask 24 -lightLinks 0 -shadowLinks 0 -fullPath-cam perspShape;')                  

def usdAssetExport(out_dir:str):

    render_his:list=cmds.ls("|root|geo|render")
    if len(render_his) > 0:
        usdAssetExport_render(out_dir)
    else:
        return False
    return True