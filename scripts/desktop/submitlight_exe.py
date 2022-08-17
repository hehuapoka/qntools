# -*- coding: utf-8 -*-
import sys,json,os,re
from typing import overload
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QThread,QRect
from submitlight_ui import Ui_Widget

#init
sys.path.append(os.path.dirname(__file__)+"/../libs")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

#init
from qn.env import plugin_root
from qn.qnui import MainListItem


import cgtw2



import qnusdtool_py as qn_py
from qn.cgtwtool import (addProjectCombox,addScCombobox,addShotCombobox,addShotCfxVerCombobox,addShotVfxVerCombobox,addShotAnimVerCombobox,addShotLightVerCombobox)
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
        pass
        # need= []
        # need_publish_usd=[]
        # need_publish_mov=[]

        # for i in self.c_l["files"]:
        #     if i['type'] == 0:
        #         qn_py.ConvertShotUSD(i['path'] ,qn_py.USDTYPE.ANIM,i['normal'])
        #         new_f = self.getrel(i['path'])
        #         if os.path.exists(new_f):
        #             need.append(qn_py.AnimCompositionInfo(qn_py.USDTYPE.ANIM,self.getname(new_f),i['asset'],new_f))
        #             need_publish_usd.append(self.gettemprel(i['path']))
            
        #     elif i['type'] == 2:
        #         qn_py.ConvertShotUSD(i['path'] ,qn_py.USDTYPE.MOV,True)
        #         need_publish_mov.append(self.gettemprel(i['path']))


        # out_anim_layer = f"./temp/{self.SC}_{self.Shot}_Cfx.usda"
        # qn_py.ConvertShotCfxLayer(need, out_anim_layer)
        # need_publish_usd.append(out_anim_layer)

        # if len(need_publish_usd) > 0:
        #     if self._ver == 0:
        #         self._tw.task.publish(db=self._db,module='shot',id=self._id,path_list=need_publish_usd,filebox_sign="cfx_mesh",note=self._note)
        #     else:
        #         self._tw.task.publish(db=self._db,module='shot',id=self._id,path_list=need_publish_usd,filebox_sign="cfx_mesh",version=f"{self._ver:03}",note=self._note)
        

        

    

class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("解算提交")

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

            m_u=re.match(r".+\.usd[ac]*$",i,re.I)
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
            addShotAnimVerCombobox(self._tw,self.ui.anim_ver,data['project.database'],shot['id'],True)
            addShotCfxVerCombobox(self._tw,self.ui.cfx_ver,data['project.database'],shot['id'],True)
            addShotVfxVerCombobox(self._tw,self.ui.vfx_ver,data['project.database'],shot['id'],True)
            addShotLightVerCombobox(self._tw,self.ui.ver,data['project.database'],shot['id'])

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
                    'normal':widget.normal.checkState() == Qt.CheckState.Checked
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
