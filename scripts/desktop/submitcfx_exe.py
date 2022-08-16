# -*- coding: utf-8 -*-
import sys,json,os,re
from typing import overload
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QThread,QRect
from submitshot_ui import Ui_Widget

#init
plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/../libs")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

import cgtw2
# t_tw = cgtw2.tw()
import qnusdtool_py as qn_py
from qn.cgtwtool import (addProjectCombox,addScCombobox,addShotCombobox,addShotCfxVerCombobox)
from qn.qnassettool import CacheUSDInAssetLibs

class MainTask(QThread):
    def __init__(self,tw:cgtw2.tw,convert_list:dict,parent=None) -> None:
        super().__init__(parent)

        self._tw=tw
        self._db=convert_list["db"]
        self._id=convert_list["id"]
        self._note=convert_list["note"]
        self._ver=convert_list["ver"]



        self.c_l = convert_list
        self.SC = convert_list["sc"]
        self.Shot = convert_list["shot"]
        
    def getrel(self,path:str):
        return "./"+os.path.basename(path)
    def gettemprel(self,path:str):
        return "./temp/"+os.path.basename(path)
    def getname(self,path:str):
        return os.path.basename(path).split(".")[0]
    def run(self):
        need= []
        need_publish_usd=[]
        need_publish_mov=[]

        for i in self.c_l["files"]:
            if i['type'] == 0:
                qn_py.ConvertShotUSD(i['path'] ,qn_py.USDTYPE.ANIM,True)
                new_f = self.getrel(i['path'])
                if os.path.exists(new_f):
                    need.append(qn_py.AnimCompositionInfo(qn_py.USDTYPE.ANIM,self.getname(new_f),i['asset'],new_f))
                    need_publish_usd.append(self.gettemprel(i['path']))
            
            elif i['type'] == 2:
                qn_py.ConvertShotUSD(i['path'] ,qn_py.USDTYPE.MOV,True)
                need_publish_mov.append(self.gettemprel(i['path']))


        out_anim_layer = f"./temp/{self.SC}_{self.Shot}_Cfx.usda"
        qn_py.ConvertShotAnimLayer(need, out_anim_layer)
        

        

        

class MainListItem(QWidget):
    _class = 0
    def __init__(self, parent=None,label="",add_type=0) -> None:
        super().__init__(parent)
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

        self.anim_type.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Fixed)
        self.anim_type.setMaximumWidth(80)
        self.anim_type.setStyleSheet("""QComboBox{border:0;background-color: #00000000;}
                                        QComboBox::drop-down{border-style: none;}
                                    """)


        self.label = QLabel(label,self)


        self.normal = QCheckBox(self)
        self.normal.setCheckState(Qt.CheckState.Unchecked)
        self.normal.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        self.space= QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.check,1)
        self.main_layout.addWidget(self.anim_type,2)
        self.main_layout.addWidget(self.label,10)
        self.main_layout.addItem(self.space)
        self.main_layout.addWidget(self.normal)
        self.setLayout(self.main_layout)
        self.setStyleSheet("padding:0;")

class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("动画提交")

        self._tw = cgtw2.tw()

        self.init()

        self.ui.proj.currentIndexChanged.connect(self.updateSc)
        self.ui.sc.currentIndexChanged.connect(self.updateShot)
        self.ui.shot.currentIndexChanged.connect(self.updateVer)

        self.ui.submit.clicked.connect(self.run)

    def init(self):

        for i in os.listdir(".\\"):
            if not os.path.isfile(i):
                continue

            m_u=re.match(r"(Chars|Elements|Props)_([a-z]+)_[0-9]+\.usd$",i,re.I)
            m_v=re.match(r".+\.mov$",i,re.I)

            if m_u:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=0)
                v.setSizeHint(d.sizeHint())
                self.ui.usd.addItem(v)
                self.ui.usd.setItemWidget(v,d)

            if m_v:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=2)
                v.setSizeHint(d.sizeHint())
                self.ui.usd.addItem(v)
                self.ui.usd.setItemWidget(v,d)
        self.initProj()
        self.updateSc()
    def initProj(self):
        addProjectCombox(self._tw,self.ui.proj)
    def updateSc(self,idx:int=0):
        data = self.ui.proj.currentData()
        if data != None:
            addScCombobox(self._tw,self.ui.sc,data['project.database'])
    def updateShot(self,idx:int=0):
        data = self.ui.proj.currentData()
        sc = self.ui.sc.currentData()
        if data != None and sc != None:
            addShotCombobox(self._tw,self.ui.shot,data['project.database'],sc['id'])

    def updateVer(self,idx:int=0):
        data = self.ui.proj.currentData()
        shot = self.ui.shot.currentData()
        if data != None and shot != None:
            addShotCfxVerCombobox(self._tw,self.ui.ver,data['project.database'],shot['id'])

    def run(self):
        if self.ui.shot.currentData() == None or  self.ui.ver.count() < 1 or self.ui.sc.currentData() == None:
            QMessageBox.warning(self,"提示","不能提交因为没用匹配的任务")
            return
        if QMessageBox.StandardButton.Yes != QMessageBox.question(self,"询问","你确定要提交吗?"):
            return
        self.ui.node.setDisabled(True)
        self.ui.submit.setDisabled(True)

        db = self.ui.proj.currentData()['project.database']
        data={"db":db,"id":self.ui.ver.currentData(),"sc":self.ui.shot.currentData()['seq.entity'],"shot":self.ui.shot.currentData()['shot.entity'],"ver":self.ui.ver.currentIndex(),"note":self.ui.node.toPlainText(),"files":[]}
        
        

        for i in range(self.ui.usd.count()):
            item =self.ui.usd.item(i)
            widget:MainListItem = self.ui.usd.itemWidget(item)
            p =os.path.abspath(".\\"+widget.label.text())
            if widget.check.checkState() == Qt.Checked: 
                data["files"].append({
                    "path":p,
                    "type":widget._class,
                    'asset':"",
                })
            
        if len(data) >0:
            self._task=MainTask(self._tw,data,self)
            self._task.finished.connect(self.taskFinished)
            self._task.start()
    def taskFinished(self):
        self.ui.node.setDisabled(False)
        self.ui.submit.setDisabled(False)
        if self._task != None:
            self._task.deleteLater()
            self._task=None
        QMessageBox.information(self,"提示","任务完成")

if __name__ == "__main__":
    app= QApplication()
    win = MainWin()
    win.setWindowIcon(QIcon(f"{plugin_root}/icon/asset.png"))
    win.show()
    sys.exit(app.exec())
