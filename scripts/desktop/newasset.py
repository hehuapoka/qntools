# -*- coding: utf-8 -*-
import sys,json,os

#init
plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/..")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

import cgtw2
t_tw = cgtw2.tw()


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NewAsset(object):
    def setupUi(self, NewAsset):
        if not NewAsset.objectName():
            NewAsset.setObjectName(u"NewAsset")
        NewAsset.resize(400, 168)
        self.verticalLayout = QVBoxLayout(NewAsset)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(NewAsset)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.proj = QComboBox(NewAsset)
        self.proj.setObjectName(u"proj")

        self.verticalLayout.addWidget(self.proj)

        self.label_2 = QLabel(NewAsset)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.asset = QComboBox(NewAsset)
        self.asset.setObjectName(u"asset")

        self.verticalLayout.addWidget(self.asset)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(NewAsset)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(NewAsset)

        QMetaObject.connectSlotsByName(NewAsset)
    # setupUi

    def retranslateUi(self, NewAsset):
        NewAsset.setWindowTitle(QCoreApplication.translate("NewAsset", u"创建USD资产", None))
        self.label.setText(QCoreApplication.translate("NewAsset", u"\u9879\u76ee", None))
        self.label_2.setText(QCoreApplication.translate("NewAsset", u"\u8d44\u4ea7", None))
        self.pushButton.setText(QCoreApplication.translate("NewAsset", u"\u6267\u884c", None))
    # retranslateUi
class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_NewAsset()
        self.ui.setupUi(self)
        self.t_projs = None
        self.asset_info = dict()
        self.init()
        self.ui.proj.currentIndexChanged.connect(self.updateAsset)

        #
        self.ui.pushButton.clicked.connect(self.run)
    def init(self):
        t_id_list =  t_tw.info.get_id(db='public', module='project', filter_list=[['project.status','=','Active']])
        self.t_projs = t_tw.info.get(db='public', module='project', id_list=t_id_list, field_sign_list=['project.entity','project.database','project.template','project.full_name'])

        #init proj
        for p in self.t_projs:
            if p['project.template'] == "千鸟动画模板Katana":
                # {'project.entity': 'LDSF', 'project.database': 'proj_ldsf', 'id': '1A99F25C-BACA-442D-9892-8A8CD11DA2D3'}
                a=self.ui.proj.addItem(f'{p["project.full_name"]}/{p["project.entity"]}',userData=p)
        
        if self.ui.proj.count() > 0:
            self.updateAsset()
    def updateAsset(self,idx=0):
        p=self.ui.proj.currentData()
        if p != None:
            self.ui.asset.clear()
            t_id_list=t_tw.info.get_id(db=p['project.database'],module='asset',filter_list=[])
            a=t_tw.info.get(db=p['project.database'],module='asset',id_list=t_id_list,field_sign_list=['asset.entity','asset.cn_name','asset.link_asset_type'])
            for i in a:
                # [{'asset.entity': 'tabel', 'id': '50CE5D5B-03C5-54A4-2AF2-A02E777430FB'}]
                if i['asset.link_asset_type'] != "Sets":
                    self.ui.asset.addItem(f'{i["asset.link_asset_type"]}/{i["asset.cn_name"]}/{i["asset.entity"]}',i)
    def run(self):
        if self.ui.asset.count() <= 0:
            return
        self.asset_info = dict()
        dir=t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=[self.ui.asset.currentData()["id"]],folder_sign_list=["asset","tex_usd","mod_usd","tex_maya"])[0]
        self.asset_info["type"] = "Asset"
        self.asset_info["project"] = self.ui.proj.currentData()
        self.asset_info["asset"] = self.ui.asset.currentData()
        self.asset_info["directory"] = dir

        with open("config.json","w+") as pf:
            pf.write(json.dumps(self.asset_info,indent=2))
        
        a.quit()
        

if __name__ == "__main__":
    a= QApplication()
    win = MainWin()
    win.setWindowIcon(QIcon(f"{plugin_root}/icon/asset.png"))
    win.show()
    sys.exit(a.exec())
