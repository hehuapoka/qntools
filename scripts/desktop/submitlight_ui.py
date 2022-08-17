# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '生成渲染文件RWQMLW.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(656, 723)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setMaximumSize(QSize(10000, 10000))
        Widget.setSizeIncrement(QSize(200, 400))
        Widget.setBaseSize(QSize(200, 400))
        Widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proj = QComboBox(Widget)
        self.proj.setObjectName(u"proj")

        self.horizontalLayout.addWidget(self.proj)

        self.sc = QComboBox(Widget)
        self.sc.setObjectName(u"sc")

        self.horizontalLayout.addWidget(self.sc)

        self.shot = QComboBox(Widget)
        self.shot.setObjectName(u"shot")

        self.horizontalLayout.addWidget(self.shot)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.usd = QListWidget(Widget)
        self.usd.setObjectName(u"usd")
        self.usd.setStyleSheet(u"border:0;\n"
"border-radius:20;")

        self.verticalLayout.addWidget(self.usd)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.anim_ver = QComboBox(self.tab)
        self.anim_ver.setObjectName(u"anim_ver")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.anim_ver)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.cfx_ver = QComboBox(self.tab)
        self.cfx_ver.setObjectName(u"cfx_ver")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cfx_ver)

        self.vfx_ver = QComboBox(self.tab)
        self.vfx_ver.setObjectName(u"vfx_ver")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.vfx_ver)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(47, 70, 112);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(26, 61, 54);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ver = QComboBox(self.tab_2)
        self.ver.setObjectName(u"ver")

        self.verticalLayout_6.addWidget(self.ver)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.node = QTextEdit(self.groupBox)
        self.node.setObjectName(u"node")
        self.node.setStyleSheet(u"border:0;")

        self.verticalLayout_3.addWidget(self.node)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.submit = QPushButton(self.tab_2)
        self.submit.setObjectName(u"submit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy1)
        self.submit.setMinimumSize(QSize(0, 40))
        self.submit.setMaximumSize(QSize(16777215, 40))
        self.submit.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(47, 70, 112);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(26, 61, 54);\n"
"}")
        self.submit.setFlat(False)

        self.verticalLayout_6.addWidget(self.submit)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 5)

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u63d0\u4ea4\u706f\u5149", None))
        self.proj.setPlaceholderText(QCoreApplication.translate("Widget", u"\u5de5\u7a0b", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u52a8\u753b\u7248\u672c", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u89e3\u7b97\u7248\u672c", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u7279\u6548\u7248\u672c", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u751f\u6210\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u751f\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u63d0\u4ea4\u8bf4\u660e", None))
        self.submit.setText(QCoreApplication.translate("Widget", u"\u63d0\u4ea4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u63d0\u4ea4", None))
    # retranslateUi

