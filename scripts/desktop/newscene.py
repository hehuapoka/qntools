# -*- coding: utf-8 -*-
from statistics import variance
import sys,json,os



plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/..")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))




import cgtw2
t_tw = cgtw2.tw()

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerHsDACG.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QContextMenuEvent,QAction)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,QTreeWidgetItemIterator,
    QVBoxLayout, QWidget,QMenu)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '新的USD场景2YLEmdq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_NewScene(object):
    def setupUi(self, NewScene):
        if not NewScene.objectName():
            NewScene.setObjectName(u"NewScene")
        NewScene.resize(748, 485)
        self.verticalLayout_2 = QVBoxLayout(NewScene)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(NewScene)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.proj = QComboBox(NewScene)
        self.proj.setObjectName(u"proj")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.proj)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.groupBox_2 = QGroupBox(NewScene)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(NewScene)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.treeWidget = QTreeWidget(self.groupBox)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_3.addWidget(self.treeWidget)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.submit = QPushButton(NewScene)
        self.submit.setObjectName(u"submit")

        self.verticalLayout_2.addWidget(self.submit)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 5)

        self.retranslateUi(NewScene)

        QMetaObject.connectSlotsByName(NewScene)
    # setupUi

    def retranslateUi(self, NewScene):
        NewScene.setWindowTitle(QCoreApplication.translate("NewScene", u"\u521b\u5efa\u573a\u666f", None))
        self.label.setText(QCoreApplication.translate("NewScene", u"\u5de5\u7a0b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewScene", u"\u5efa\u9020\u573a\u666f", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewScene", u"\u4f9d\u8d56\u8d44\u4ea7", None))
        self.submit.setText(QCoreApplication.translate("NewScene", u"\u66f4\u65b0\u914d\u7f6e", None))
    # retranslateUi









class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_NewScene()
        self.ui.setupUi(self)
        self.ui.treeWidget.setSelectionMode(QTreeWidget.ExtendedSelection)

        self.menu=QMenu(self)
        a=QAction("勾选选择资产",self)
        a.triggered.connect(self.setCheckForSelected)
        self.menu.addAction(a)

        self.data = None
        self.init()

        self.ui.proj.currentIndexChanged.connect(self.updateAsset)

        self.ui.submit.clicked.connect(self.run)

    def init(self):
        self.initProj()
        self.updateAsset()
        self.readConfig()
    def initProj(self):
        t_id_list =  t_tw.info.get_id(db='public', module='project', filter_list=[['project.status','=','Active']])
        self.t_projs = t_tw.info.get(db='public', module='project', id_list=t_id_list, field_sign_list=['project.entity','project.database','project.template','project.full_name'])

        #init proj
        for p in self.t_projs:
            if p['project.template'] == "千鸟动画模板Katana":
                # {'project.entity': 'LDSF', 'project.database': 'proj_ldsf', 'id': '1A99F25C-BACA-442D-9892-8A8CD11DA2D3'}
                a=self.ui.proj.addItem(f'{p["project.full_name"]}({p["project.entity"]})',userData=p)
        
        try:
            with open("config.json","r") as pf:
                self.data = json.loads(pf.read())
        except:
            pass

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        self.menu.exec(QCursor.pos())
        return super().contextMenuEvent(event)

    def setCheckForSelected(self):
        for item in self.ui.treeWidget.selectedItems():
            if item.parent() != None:
                item.setCheckState(0,Qt.Checked)
                    

    ############
    def updateAsset(self,idx=0):
        p=self.ui.proj.currentData()
        if p != None:
            self.ui.treeWidget.clear()
            self.ui.listWidget.clear()
            t_id_list=t_tw.info.get_id(db=p['project.database'],module='asset',filter_list=[])
            a=t_tw.info.get(db=p['project.database'],module='asset',id_list=t_id_list,field_sign_list=['asset.entity','asset.cn_name','asset.link_asset_type'])

            #init frist
            self.ui.treeWidget.setHeaderLabels(["名称","中文名称","ID"])
            char = QTreeWidgetItem(self.ui.treeWidget,["Chars","角色"])
            prop = QTreeWidgetItem(self.ui.treeWidget,["Props","道具"])
            elem = QTreeWidgetItem(self.ui.treeWidget,["Elems","元素"])
            scene = QTreeWidgetItem(self.ui.treeWidget,["Sets","场景"])

            char.setIcon(0,QIcon(f"{plugin_root}/icon/char.png"))
            prop.setIcon(0,QIcon(f"{plugin_root}/icon/prop.png"))
            elem.setIcon(0,QIcon(f"{plugin_root}/icon/elem.png"))
            scene.setIcon(0,QIcon(f"{plugin_root}/icon/scene.png"))

            for i in a:
                # [{'asset.entity': 'tabel', 'id': '50CE5D5B-03C5-54A4-2AF2-A02E777430FB'}]
                if i['asset.link_asset_type'] == "Sets":
                    l_item = QListWidgetItem(QIcon(f"{plugin_root}/icon/scene.png"),i["asset.entity"],self.ui.listWidget)
                    l_item.setCheckState(Qt.Unchecked)
                    l_item.setData(3,i)

                    item = QTreeWidgetItem(scene,[i["asset.entity"],i["asset.cn_name"],i["id"]])
                    item.setCheckState(0,Qt.Unchecked)
                elif i['asset.link_asset_type'] == "Chars":
                    item = QTreeWidgetItem(char,[i["asset.entity"],i["asset.cn_name"],i["id"]])
                    item.setCheckState(0,Qt.Unchecked)

                elif i['asset.link_asset_type'] == "Props":
                    item = QTreeWidgetItem(prop,[i["asset.entity"],i["asset.cn_name"],i["id"]])
                    item.setCheckState(0,Qt.Unchecked)

                elif i['asset.link_asset_type'] == "Elements":
                    item = QTreeWidgetItem(elem,[i["asset.entity"],i["asset.cn_name"],i["id"]])
                    item.setCheckState(0,Qt.Unchecked)


    def readConfig(self):
        if self.data != None:
            config_data = self.data
            for xx in range(self.ui.proj.count()):
                if self.ui.proj.itemData(xx)['id'] == self.data['project']['id']:

                    self.ui.proj.setCurrentIndex(xx)
                    self.updateAsset()

                    for i in range(self.ui.listWidget.count()):
                        
                        l_item = self.ui.listWidget.item(i)
                        id = l_item.data(3)['id']
                        for j in config_data['asset']:
                            if j['id'] == id:
                                l_item.setCheckState(Qt.Checked)
                                break


                    item = QTreeWidgetItemIterator(self.ui.treeWidget)
                    while item.value():
                        v=item.value()
                        if v != None:
                            tx = v.text(2)
                            for bb in config_data['links']:
                                if tx == bb['id']:
                                    v.setCheckState(0,Qt.Checked)
                                    break
                        item += 1
                break


    def run(self):
        if self.ui.listWidget.count() <= 0:
            return
        ids = []
        item = QTreeWidgetItemIterator(self.ui.treeWidget,QTreeWidgetItemIterator.Checked)
        while item.value():
            v=item.value()
            if v != None:
                ids.append(v.text(2))
            item += 1
        asset_info = dict()
        link_asset=t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=ids,folder_sign_list=["asset"])

        asset_info["type"] = "Scene"
        asset_info["project"] = self.ui.proj.currentData()

        #########################
        sss = []
        for idk in range(self.ui.listWidget.count()):
            itt =self.ui.listWidget.item(idk)
            if itt.checkState() == Qt.Checked:

                bb = dict()
                sss.append(itt.data(3))
        asset_info["asset"]=sss
        ###########################

        asset_info["links"] = link_asset

        with open("config.json","w+") as pf:
            pf.write(json.dumps(asset_info,indent=2))
        a.quit()
if __name__ == "__main__":
    a= QApplication()
    win = MainWin()
    win.setWindowIcon(QIcon(f"{plugin_root}/icon/scene.png"))
    win.show()
    sys.exit(a.exec())
