from imp import reload
import sys,os
import json
import maya.mel as mel
import maya.cmds as cmds


_mayap = os.path.join(os.environ['QNTOOLS'],"scripts\\maya").replace("\\","/")
if _mayap not in sys.path:
    sys.path.append(_mayap)
try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import (QIcon,QPixmap)
    from PySide6.QtCore  import (QSize,Qt)
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import (QIcon,QPixmap)
    from PySide2.QtCore  import (QSize,Qt)

import usdexport_ui
reload(usdexport_ui)


#initconfig.run()
from qn_maya import envUtils

reload(envUtils)


import maya.utils as Mthread
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
maya_win= wrapInstance(int(mayaMainWindowPtr), QWidget)


def runThread():
    try:
        cmds.select("|root",r=True)
    except:
        QMessageBox.warning(maya_win,u"警告","该场景未包含|root层级")
        return
    a=QFileDialog.getSaveFileName(maya_win,u"设置保存文件","D:/test","USD File (*.usd)")
    if a[0] != "":
        mel.eval('file -force -options ";exportUVs=1;exportSkels=none;exportSkin=none;exportBlendShapes=0;exportDisplayColor=0;;exportColorSets=1;defaultMeshScheme=none;animation=0;eulerFilter=0;staticSingleSample=0;startTime=0;endTime=1143;frameStride=1;frameSample=0.0;defaultUSDFormat=usdc;parentScope=;shadingMode=none;exportInstances=1;exportVisibility=1;mergeTransformAndShape=1;stripNamespaces=1;jobContext=[Arnold]" -typ "USD Export" -pr -es "{}";'.format(a[0]))

def run():
    runThread()

if __name__ == "__main__":
    runThread()