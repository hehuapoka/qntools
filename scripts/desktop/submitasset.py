# -*- coding: utf-8 -*-
import sys,json,os

#init
plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/..")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

import cgtw2
t_tw = cgtw2.tw()

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_SubmitAsset(object):
    def setupUi(self, SubmitAsset):
        if not SubmitAsset.objectName():
            SubmitAsset.setObjectName(u"SubmitAsset")
        SubmitAsset.resize(400, 441)
        self.verticalLayout = QVBoxLayout(SubmitAsset)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(SubmitAsset)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SubmitFiles = QListWidget(self.groupBox_2)
        self.SubmitFiles.setObjectName(u"SubmitFiles")
        self.SubmitFiles.setStyleSheet(u"border-radius:2;")

        self.verticalLayout_4.addWidget(self.SubmitFiles)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(SubmitAsset)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Note = QTextEdit(self.groupBox)
        self.Note.setObjectName(u"Note")
        self.Note.setStyleSheet(u"border-radius:2;")

        self.verticalLayout_3.addWidget(self.Note)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Submit = QPushButton(SubmitAsset)
        self.Submit.setObjectName(u"Submit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Submit.sizePolicy().hasHeightForWidth())
        self.Submit.setSizePolicy(sizePolicy)
        self.Submit.setMinimumSize(QSize(80, 0))
        self.Submit.setStyleSheet(u"QPushButton{\n"
"	background-color:#00aabb;\n"
"	border-radius:6px;\n"
"	padding:2px 4px;\n"
"}")

        self.horizontalLayout.addWidget(self.Submit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SubmitAsset)

        QMetaObject.connectSlotsByName(SubmitAsset)
    # setupUi

    def retranslateUi(self, SubmitAsset):
        SubmitAsset.setWindowTitle(QCoreApplication.translate("SubmitAsset", u"\u8d44\u4ea7\u63d0\u4ea4", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SubmitAsset", u"\u4e0a\u4f20\u5217\u8868", None))
        self.groupBox.setTitle(QCoreApplication.translate("SubmitAsset", u"Note", None))
        self.Submit.setText(QCoreApplication.translate("SubmitAsset", u"\u63d0\u4ea4", None))
    # retranslateUi

class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.data=None


        self.ui = Ui_SubmitAsset()
        self.ui.setupUi(self)
        self.ui.Submit.clicked.connect(self.Run)
    

        self.init()
    def init(self):
        with open("config.json") as pf:
            self.data = json.loads(pf.read())
        try:
            fs=os.listdir("USD")
            for i in fs:
                if os.path.splitext(i)[-1] in ['.usd',".usda",".usdc"]:
                    a=QListWidgetItem(i)
                    self.ui.SubmitFiles.addItem(a)
                    a.setCheckState(Qt.Checked)
                    
                    
        except:
            pass

    def Run(self):
        a=[]
        for i in range(self.ui.SubmitFiles.count()):
            item =self.ui.SubmitFiles.item(i)
            if item.checkState() == Qt.Checked:
                a.append(os.path.abspath("USD/"+item.text()))
        if len(a) >0 and self.data != None:
            c_db=self.data['project']['project.database']
            c_id_asset = self.data['asset']['id']
            #print(self.data['project']['project.database'])
            #print(self.data['asset']['id'])
            c_id_task=t_tw.task.get_id(db=c_db, module='asset', filter_list=[["asset.id","=",c_id_asset],'and',['task.entity','=','LookDev']])[0]

            self.ui.Note.setDisabled(True)
            self.ui.Submit.setDisabled(True)

            t_tw.task.publish(db=self.data['project']['project.database'],module='asset',id=c_id_task,path_list=a,filebox_sign="usdasset",note=self.ui.Note.toPlainText())
            #print(self.ui.Note.toPlainText())
            #t_tw.task.submit(db=self.data['project']['project.database'],module='asset',id=self.data['asset']['id'],path_list=a,note=self.ui.Note.placeholderText(),submit_type='file')
            app.quit()
        

if __name__ == "__main__":
    app= QApplication()
    win = MainWin()
    win.setWindowIcon(QIcon(f"{plugin_root}/icon/asset.png"))
    win.show()
    sys.exit(app.exec())
