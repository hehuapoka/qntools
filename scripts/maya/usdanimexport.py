from imp import reload
import maya.cmds as cmds
#import pymel.core as pm
import os,re,sys

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
# reload(usdexport_ui)
import qn_maya.mayaUtils as qn_mu
#reload(qn_mu)


import maya.utils as Mthread
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
maya_win= wrapInstance(int(mayaMainWindowPtr), QWidget)


def getExportHis():
    export_his =dict()
    nts=cmds.ls(rf=True)
    for i in nts:
        a=cmds.referenceQuery(i,rfn=True,p=True)
        a_cc=cmds.referenceQuery(i,rfn=True,ch=True)
        a_il=cmds.referenceQuery(i,il=True)
        if a==None and a_il and a_cc==None:
            b = cmds.referenceQuery(i,filename=True)
            filename=os.path.basename(b)
            #asset_type=filename.split("_")[0]
            #asset_name=filename.split("_")[1:-1]

            c=re.match(r"^.+{([0-9]+)}$",filename,re.I)
            asset_num = 0
            if c != None:
                asset_num = int(c.group(1))
            
            d=re.match(r"^([a-z]+)_([a-z]+)_rig_[lch]\.[a-z].+$",filename,re.I)
            if d != None:
                ns=cmds.referenceQuery(i,ns=True)[1:]
                try:
                    export_his[f"{ns}:render"]=f"{d.group(1)}_{d.group(2)}_anim_{asset_num}.usd"
                except:
                    print(u"没有该模型层级")
    return export_his
def exportAnims(data):

    export_list=getExportHis()
    for i in export_list:
        try:
            cmds.select(i)
            out_path = os.path.join(data['path'],export_list[i]).replace("\\","/")
            qn_mu.usdExportCmd(out_path,data['sf'],data['ef'],data['c'],data['uv'],data['n'],data['mat'])
        except:
            print(u"不能导出该ref")

def exportCamera(data,cam_path):

    try:
        cmds.select(cam_path)
        out_path = os.path.join(data['path'],"main_camera.usd").replace("\\","/")
        qn_mu.usdExportCmd(out_path,data['sf'],data['ef'],data['c'],data['uv'],data['n'],data['mat'])
    except:
        print(u"不能导出该ref")
#exportAnims()


class MyWin(QWidget):
    def __init__(self,parent=None):
        super(MyWin,self).__init__(parent)

        self.ui = usdexport_ui.Ui_QNUsdExport()
        self.ui.setupUi(self)

        self.init()

        self.ui.exit.clicked.connect(self.exitWin)
        self.ui.submit.clicked.connect(self.run)
        self.ui.CameraPick.clicked.connect(self.clickCameraButton)

    def init(self):
        self.ui.uv.setChecked(Qt.CheckState.Checked)
        import maya.cmds as cmds
        default_camera = ['frontShape', 'perspShape', 'sideShape', 'topShape','backShape', 'leftShape', 'bottomShape']
        c_cam = None
        for cam in cmds.ls(ca=True):
            if cam not in default_camera:
                c_cam = cmds.listRelatives(cam,p=True)[0]
        if c_cam != None:
            self.ui.Camera.setText(c_cam)
    def clickCameraButton(self):
        try:
            sel=cmds.ls(sl=True)[0]
            self.ui.Camera.setText(sel)
        except:
            pass
            
    def exitWin(self):
        self.close()
    def run(self):
        a=QFileDialog.getExistingDirectory(self,u"设置保存文件","D:/test")
        if a != "":

            data = {"path":a,
                "sf":self.ui.start_frame.value(),
                "ef":self.ui.end_frame.value(),
                "c":self.ui.display_color.isChecked(),
                "uv":self.ui.uv.isChecked(),
                "n":self.ui.subdiv.isChecked(),
                "mat":self.ui.material.isChecked()
            }
            Mthread.executeInMainThreadWithResult(exportAnims,data)
            Mthread.executeInMainThreadWithResult(exportCamera,data,self.ui.Camera.text())

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
