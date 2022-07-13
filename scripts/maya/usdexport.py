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



import maya.utils as Mthread
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
maya_win= wrapInstance(int(mayaMainWindowPtr), QWidget)


def run_cmd(outpath,stratframe,endframe,colorsets,uvsets,normals,shaders):
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
                    chaser=['alembic'],
                    chaserArgs=[('alembic', 'attrprefix', 'asset_=asset_'),],
                    exportRoots=root_his   
                   )
def runThread(data):
    run_cmd(data['path'],data['sf'],data['ef'],data['c'],data['uv'],data['n'],data['mat'])

#run_cmd("D:/test/f.usd",1,10,False,True,False,False)

class MyWin(QWidget):
    def __init__(self,parent=None):
        super(MyWin,self).__init__(parent)

        self.ui = usdexport_ui.Ui_QNUsdExport()
        self.ui.setupUi(self)

        self.init()

        self.ui.exit.clicked.connect(self.exitWin)
        self.ui.submit.clicked.connect(self.run)

    def init(self):
        self.ui.uv.setChecked(Qt.CheckState.Checked)
    def exitWin(self):
        self.close()
    def run(self):
        if len(cmds.ls(sl=True)) < 1:
            QMessageBox.warning(self,u"警告","你没有选择如何问题不能导出")
            return
        a=QFileDialog.getSaveFileName(self,u"设置保存文件","D:/test","USD File (*.usd)")
        if a[0] != "":

            data = {"path":a[0],
                "sf":self.ui.start_frame.value(),
                "ef":self.ui.end_frame.value(),
                "c":self.ui.display_color.isChecked(),
                "uv":self.ui.uv.isChecked(),
                "n":self.ui.subdiv.isChecked(),
                "mat":self.ui.material.isChecked()
            }
            Mthread.executeInMainThreadWithResult(runThread,data)

def run():
    a=MyWin()
    a.setParent(maya_win)
    a.setWindowFlag(Qt.Window)
    a.show()

if __name__ == "__main__":
    a=MyWin()
    a.setParent(maya_win)
    a.setWindowFlag(Qt.Window)
    a.show()