#coding:utf-8
import sys,os,json
import maya.cmds as cmds
#import pymel.core as pm
import maya.mel as mel
import maya.standalone
try: 			
    maya.standalone.initialize() 		
except: 			
    pass
##################################
# def addAttrSingle(a_list:list,his:str,name:str,value,a_dt:str):
#     if name in a_list:
#          cmds.setAttr(f'{his}.{name}',l=False)
#          if a_dt == "string":
#             cmds.setAttr(f'{his}.{name}', value, type=a_dt,keyable=False, l=True )
#          else:
#             cmds.setAttr(f'{his}.{name}', value,keyable=False, l=True )
#     else:
#         if a_dt == "string":
#             cmds.addAttr(ln=name,dt=a_dt)
#             cmds.setAttr(f'{his}.{name}', value, type=a_dt,keyable=False, l=True )
#         else:
#             cmds.addAttr(ln=name,at=a_dt)
#             cmds.setAttr(f'{his}.{name}', value,keyable=False, l=True )

# def addAttrToModel(his:str):
#     cmds.select(his)
#     a_t=[
#             {"name":"asset_name","type":"string","value":_data["data"]["asset.entity"]},
#             {"name":"asset_type","type":"string","value":_data["data"]["asset.type"]},
#             {"name":"asset_number","type":"long","value":0}
#         ]
#     for i in a_t:
#         a_list=cmds.listAttr(his)
#         addAttrSingle(a_list,his,i["name"],i['value'],i['type'])
        
    
# def setMyAttr(his:str):
#     cmds.select(his)
#     all_sub=mel.eval(f'listRelatives -c -f -ad {his}')
#     addAttrToModel(his)
#     for sub in all_sub:
#         addAttrToModel(sub)

# setMyAttr("|root")


cmds.file("D:/test/a.ma",open=True,force=True)
cmds.file( "D:/test/b.ma", force=True, options="v=0;", type="mayaAscii", ea=True)



try: 			
    maya.standalone.uninitialize() 		
except: 			
    pass