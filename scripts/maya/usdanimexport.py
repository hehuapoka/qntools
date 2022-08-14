from imp import reload
import maya.cmds as cmds
import maya.mel as mel
import os,re,sys

_mayap = os.path.join(os.environ['QNTOOLS'],"scripts\\maya").replace("\\","/")
plugin_root = os.environ['QNTOOLS']

if _mayap not in sys.path:
    sys.path.append(_mayap)
try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import (QIcon,QPixmap)
    from PySide6.QtCore  import (QSize,Qt,QSettings)
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import (QIcon,QPixmap)
    from PySide2.QtCore  import (QSize,Qt,QSettings)

import usdanimexport_ui
reload(usdanimexport_ui)
import qn_maya.mayaUtils as qn_mu
reload(qn_mu)


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
                    export_his[f"{ns}:render"]=f"{d.group(1)}_{d.group(2)}_{asset_num}.usd"
                except:
                    print(u"没有该模型层级")
    return export_his
def exportAnims(data:dict,out_dir:str,s_t:int,e_t:int):

    for i in data:
        try:
            cmds.select(i)
            out_path = os.path.join(out_dir,data[i]).replace("\\","/")
            mel.eval('file -force -options ";exportUVs=1;exportSkels=none;exportSkin=none;exportBlendShapes=0;exportDisplayColor=0;;exportColorSets=0;defaultMeshScheme=none;animation=1;eulerFilter=0;staticSingleSample=0;startTime={};endTime={};frameStride=1;frameSample=0.0;defaultUSDFormat=usdc;parentScope=;shadingMode=none;exportInstances=0;exportVisibility=1;mergeTransformAndShape=1;stripNamespaces=1;jobContext=[Arnold]" -typ "USD Export" -pr -es "{}";'.format(s_t,e_t,out_path))
        except:
            print(u"不能导出该ref")



class MainListItem(QWidget):
    _class = 0
    #_data = None
    def __init__(self, parent=None,label="",add_type=0) -> None:
        super().__init__(parent)
        #self._data=None
        self._anim_icon = QIcon(f"{plugin_root}/icon/anim.png")
        self._cam_icon = QIcon(f"{plugin_root}/icon/cam.png")
        self._sc_icon = QIcon(f"{plugin_root}/icon/scene.png")
        self._video_icon = QIcon(f"{plugin_root}/icon/video.png")

        self.check = QCheckBox(self)
        self.check.setCheckState(Qt.CheckState.Checked)
        self.check.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.check.setStyleSheet("""QCheckBox::indicator
                                    {
                                        border : 1px solid #55555533;
                                        border-radius:3px;
                                    }
                                    QCheckBox::indicator::checked
                                    {
                                        background-color:#85e9ff;
                                        border : none;
                                    }
                                    """)

        self.anim_type = QComboBox(self)
        if add_type==0:
            self.anim_type.addItem(self._anim_icon,"动画")
        elif add_type == 1:
            self.anim_type.addItem(self._cam_icon,"相机")
        elif add_type == 2:
            self.anim_type.addItem(self._video_icon,"视频")
        elif add_type == 3:
            self.anim_type.addItem(self._sc_icon,"场景")
        self._class=add_type

        self.filename = QLineEdit(self)

        self.anim_type.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Fixed)
        self.anim_type.setMaximumWidth(80)
        self.anim_type.setStyleSheet("""QComboBox{border:0;background-color: #00000000;}
                                        QComboBox::drop-down{border-style: none;}
                                    """)


        self.label = QLabel(label,self)


        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.check,1)
        self.main_layout.addWidget(self.anim_type,2)
        self.main_layout.addWidget(self.label,10)
        self.main_layout.addWidget(self.filename,10)
        self.setLayout(self.main_layout)
        self.setStyleSheet("padding:0;")
        
    def setData(self,data):
        #self._data = data
        self.filename.setText(data)


class MyWin(QWidget):
    def __init__(self,parent=None):
        super(MyWin,self).__init__(parent)

        self.default_camera = ['frontShape', 'perspShape', 'sideShape', 'topShape','backShape', 'leftShape', 'bottomShape']
        self.settings=QSettings("./Setting.ini", QSettings.IniFormat)

        self.ui = usdanimexport_ui.Ui_Form()
        self.ui.setupUi(self)

        self.init()

        self.ui.pushButton.clicked.connect(self.run)


    def init(self):

        for idx,cam in enumerate(cmds.ls(ca=True)):
            if cam not in self.default_camera:
                v = QListWidgetItem()
                d = MainListItem(label=cam,add_type=1)
                d.setData(f"camera_{idx}.usd")
                v.setSizeHint(d.sizeHint())
                self.ui.listWidget.addItem(v)
                self.ui.listWidget.setItemWidget(v,d)
        anims = getExportHis()
        for anim in anims:
            v = QListWidgetItem()
            d = MainListItem(label=anim,add_type=0)
            d.setData(anims[anim])
            v.setSizeHint(d.sizeHint())
            self.ui.listWidget.addItem(v)
            self.ui.listWidget.setItemWidget(v,d)

            
    def exitWin(self):
        self.close()
    def run(self):
        a=QFileDialog.getExistingDirectory(self,u"设置保存文件",self.settings.value("LastFilePath"))
        if a != "":
            data = dict()
            for i in range(self.ui.listWidget.count()):
                item =self.ui.listWidget.item(i)
                widget:MainListItem = self.ui.listWidget.itemWidget(item)
                if widget.check.checkState() == Qt.Checked: 
                    data[widget.label.text()]=widget.filename.text()
            
            Mthread.executeInMainThreadWithResult(exportAnims,data,a,self.ui.st.value(),self.ui.et.value())

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
