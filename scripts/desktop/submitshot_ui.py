# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '上传动画WcuQlu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

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

        self.ver = QComboBox(Widget)
        self.ver.setObjectName(u"ver")

        self.horizontalLayout.addWidget(self.ver)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usd = QListWidget(Widget)
        self.usd.setObjectName(u"usd")

        self.verticalLayout_2.addWidget(self.usd)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.node = QTextEdit(self.groupBox)
        self.node.setObjectName(u"node")
        self.node.setStyleSheet(u"border:0;")

        self.verticalLayout_3.addWidget(self.node)


        self.verticalLayout.addWidget(self.groupBox)

        self.submit = QPushButton(Widget)
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

        self.verticalLayout.addWidget(self.submit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.proj.setPlaceholderText(QCoreApplication.translate("Widget", u"\u5de5\u7a0b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u63d0\u4ea4\u8bf4\u660e", None))
        self.submit.setText(QCoreApplication.translate("Widget", u"\u63d0\u4ea4", None))
    # retranslateUi

