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
from qn.cgtwtool import (addProjectCombox,addScCombobox,addShotCombobox,addShotAnimVerCombobox)
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


        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.check,1)
        self.main_layout.addWidget(self.anim_type,2)
        self.main_layout.addWidget(self.label,10)
        self.setLayout(self.main_layout)
        self.setStyleSheet("padding:0;")

class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

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
            m_c=re.match(r"Camera_[0-9]+\.usd$",i,re.I)
            m_v=re.match(r".+\.mov$",i,re.I)
            m_s=re.match(r"Scene_Anim.usd$",i,re.I)
            if m_u:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=0)
                v.setSizeHint(d.sizeHint())
                self.ui.usd.addItem(v)
                self.ui.usd.setItemWidget(v,d)
            if m_c:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=1)
                v.setSizeHint(d.sizeHint())
                self.ui.usd.addItem(v)
                self.ui.usd.setItemWidget(v,d)
            
            if m_v:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=2)
                v.setSizeHint(d.sizeHint())
                self.ui.usd.addItem(v)
                self.ui.usd.setItemWidget(v,d)
            if m_s:
                v = QListWidgetItem()
                d = MainListItem(label=i,add_type=3)
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
            addShotAnimVerCombobox(self._tw,self.ui.ver,data['project.database'],shot['id'])

    def run(self):
        if self.ui.shot.currentData() == None or  self.ui.ver.count() < 1:
            QMessageBox.warning(self,"提示","不能提交因为没用匹配的任务")
            return
        if QMessageBox.StandardButton.Yes != QMessageBox.question(self,"询问","你确定要提交吗?"):
            return
        self.ui.node.setDisabled(True)
        self.ui.submit.setDisabled(True)

        data={"id":self.ui.ver.currentData(),"ver":self.ui.ver.currentText(),"files":[]}
        

        for i in range(self.ui.usd.count()):
            item =self.ui.usd.item(i)
            widget:MainListItem = self.ui.usd.itemWidget(item)
            if widget.check.checkState() == Qt.Checked: 
                data["files"].append({
                    "path":os.path.abspath(".\\"+widget.label.text()),
                    "type":widget._class,
                    'rename':"",
                })
            
        if len(data) >0:
            print(data)
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
