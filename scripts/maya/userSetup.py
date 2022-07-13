#encoding=utf8
import pymel.core as pm
import maya.mel as mel
import sys
import os,re

def run():
    try:
        _mayap = os.path.join(os.environ['QNTOOLS'],"scripts\\maya").replace("\\","/")
        if _mayap not in sys.path:
            sys.path.append(_mayap)

        main_window=pm.language.melGlobals['gMainWindow']
        menu_obj = "gbwz"
        menu_label=u"GBWZToolSets"
        if pm.menu(menu_obj,label=menu_label,exists=True,parent=main_window):
            pm.deleteUI(pm.menu(menu_obj,e=True,deleteAllItems=True))
        custum_tools_menu=pm.menu(menu_obj,label=menu_label,parent=main_window,tearOff=True)

        pm.menuItem(label=u'资产读取',command="import assetloader\nassetloader.run()")
        pm.menuItem(label=u'导出当前选择',command="import usdexport\nusdexport.run()")
        
        pm.menuItem( divider=True )

        pm.menuItem(label=u'资产工具',subMenu=True)
        pm.menuItem(label=u'创建层级模板',command="from qn.mayaUtils import createModelHierarchy\ncreateModelHierarchy()")

        pm.setParent( '..', menu=True )
        pm.menuItem(label=u'动画工具',subMenu=True)
        pm.menuItem(label=u'导出动画',command="import usdanimexport\nusdanimexport.run()")
        pm.menuItem(label=u'动画拍平')

        pm.setParent( '..', menu=True )
        pm.menuItem(label=u'解算工具',subMenu=True)
        pm.menuItem(label=u'导出角色布料')
        pm.menuItem(label=u'导出角色毛发')
    except:
        print("plus in loading error")
        
        
        
        

pm.evalDeferred("run()")