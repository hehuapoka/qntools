# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerNEHfiQ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from PySide6.QtCore  import *
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore  import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(742, 623)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.st = QSpinBox(Form)
        self.st.setObjectName(u"st")
        self.st.setMinimum(-10000)
        self.st.setMaximum(10000)
        self.st.setValue(1001)

        self.horizontalLayout.addWidget(self.st)

        self.et = QSpinBox(Form)
        self.et.setObjectName(u"et")
        self.et.setMinimum(-10000)
        self.et.setMaximum(10000)
        self.et.setValue(1010)

        self.horizontalLayout.addWidget(self.et)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u52a8\u753b", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
    # retranslateUi

