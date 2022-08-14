# -*- coding: utf-8 -*-
import sys,json,os,re
from typing import overload
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QThread
from submitasset_ui import Ui_Widget

#init
plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/..")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

import cgtw2
# t_tw = cgtw2.tw()


class MainTask(QThread):
    def __init__(self, tw:cgtw2.tw,db,id,note:str,usd:list,img:list,parent=None) -> None:
        super().__init__(parent)
        self._usd = usd
        self._img = img
        self._tw = tw
        self._db = db
        self._id = id
        self._note = note

    def run(self): 

        if len(self._usd) > 0:
            self._tw.task.publish(db=self._db,module='asset',id=self._id,path_list=self._usd,filebox_sign="asset_tex_usd",note=self._note)
        if len(self._img) > 0:
            self._tw.task.publish(db=self._db,module='asset',id=self._id,path_list=self._img,filebox_sign="asset_tex",note=self._note)


class MainWin(QWidget):
    _asset_name=None
    _asset_type=None
    _tw =None
    _task = None
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.init()

        self.ui.radUsd.toggled.connect(self.changeUsdCheck)
        self.ui.radImg.toggled.connect(self.changeImgCheck)
        self.ui.submit.clicked.connect(self.run)

        self.ui.proj.currentIndexChanged.connect(self.updateAsset)

    def init(self):
        self._tw = cgtw2.tw()

        self.ui.usd.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.img.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #init parm


        a = [".usd",".usda",".usdc"]
        for i in os.listdir(".\\"):
            if not os.path.isfile(i):
                continue
            if os.path.splitext(i)[-1] not in a:
                continue
            k=QListWidgetItem(i,self.ui.usd)
            k.setCheckState(Qt.CheckState.Checked)

            m=re.match(r"(Chars|Elements|Props)_([a-z]+)\.usda",i,re.I)
            if m:
                self._asset_name = m.group(2)
                self._asset_type = m.group(1)

        if not os.path.exists(".\\Textures"): return

        for i in os.listdir(".\\Textures"):
            if not os.path.isfile(".\\Textures\\"+i):
                continue
            if os.path.splitext(i)[-1] != ".tx":
                continue
            k=QListWidgetItem(i,self.ui.img)
            k.setCheckState(Qt.CheckState.Checked)

        

        self.initProj()
        self.updateAsset()

    def changeUsdCheck(self,check:bool):
        if check:
            for i in range(self.ui.usd.count()):
                self.ui.usd.item(i).setCheckState(Qt.Checked.Checked)
        else:
            for i in range(self.ui.usd.count()):
                self.ui.usd.item(i).setCheckState(Qt.Checked.Unchecked)
    def changeImgCheck(self,check:bool):
        if check:
            for i in range(self.ui.img.count()):
                self.ui.img.item(i).setCheckState(Qt.Checked.Checked)
        else:
            for i in range(self.ui.img.count()):
                self.ui.img.item(i).setCheckState(Qt.Checked.Unchecked)
    def checkAssetVersion(self):
        pass
    def initProj(self):
        t_id_list =  self._tw.info.get_id(db='public', module='project', filter_list=[['project.status','=','Active']])
        self.t_projs = self._tw.info.get(db='public', module='project', id_list=t_id_list, field_sign_list=['project.entity','project.database','project.template','project.full_name'])

        #init proj
        for p in self.t_projs:
            if p['project.template'] == "千鸟动画模板Katana":
                # {'project.entity': 'LDSF', 'project.database': 'proj_ldsf', 'id': '1A99F25C-BACA-442D-9892-8A8CD11DA2D3'}
                a=self.ui.proj.addItem(f'{p["project.full_name"]}',userData=p)
        

    def updateAsset(self,idx=0):
        p=self.ui.proj.currentData()
        if p != None:
            self.ui.asset.clear()

            t_id_list=self._tw.info.get_id(db=p['project.database'],module='asset',filter_list=[])
            a=self._tw.info.get(db=p['project.database'],module='asset',id_list=t_id_list,field_sign_list=['asset.entity','asset.cn_name','asset.link_asset_type'])

            #init frist
            for i in a:
                if i['asset.link_asset_type'] != "Sets":
                    self.ui.asset.addItem(f'{i["asset.link_asset_type"]}_{i["asset.entity"]}',userData=i)
            
            k=self.ui.asset.findText(f"{self._asset_type}_{self._asset_name}")
            if k != -1:
                self.ui.asset.setCurrentIndex(k)

    def run(self):
        if self.ui.asset.currentText() != f"{self._asset_type}_{self._asset_name}":
            QMessageBox.warning(self,"提示","不能提交因为文件名称不符合规范")
            return
        if QMessageBox.StandardButton.Yes != QMessageBox.question(self,"询问","你确定要提交吗?"):
            return
        self.ui.node.setDisabled(True)
        self.ui.submit.setDisabled(True)

        usd=[]
        img=[]

        for i in range(self.ui.usd.count()):
            item =self.ui.usd.item(i)
            if item.checkState() == Qt.Checked:
                usd.append(os.path.abspath(".\\"+item.text()))
        
        for i in range(self.ui.img.count()):
            item =self.ui.img.item(i)
            if item.checkState() == Qt.Checked:
                img.append(os.path.abspath(".\\Textures\\"+item.text()))
            
        if (len(usd) >0 or len(img) >0 ) and self.ui.asset.currentData() != None:
            c_db=self.ui.proj.currentData()['project.database']
            c_id_asset = self.ui.asset.currentData()['id']
            c_id_task=self._tw.task.get_id(db=c_db, module='asset', filter_list=[["asset.id","=",c_id_asset],'and',['task.entity','=','Texture']])[0]
            
            self._task=MainTask(self._tw,c_db,c_id_task,self.ui.node.toPlainText(),usd,img,self)
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
