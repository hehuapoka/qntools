# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetwWDRYz.ui'
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
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(298, 369)
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
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"background-color: rgb(66, 211, 255);\n"
"padding:5px;")

        self.horizontalLayout.addWidget(self.label)

        self.version = QComboBox(Widget)
        self.version.setObjectName(u"version")

        self.horizontalLayout.addWidget(self.version)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.img = QListWidget(Widget)
        self.img.setObjectName(u"img")

        self.verticalLayout_2.addWidget(self.img)

        self.usd = QListWidget(Widget)
        self.usd.setObjectName(u"usd")

        self.verticalLayout_2.addWidget(self.usd)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radUsd = QCheckBox(Widget)
        self.radUsd.setObjectName(u"radUsd")

        self.horizontalLayout_2.addWidget(self.radUsd)

        self.radImg = QCheckBox(Widget)
        self.radImg.setObjectName(u"radImg")

        self.horizontalLayout_2.addWidget(self.radImg)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.submit = QPushButton(Widget)
        self.submit.setObjectName(u"submit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy2)
        self.submit.setMinimumSize(QSize(0, 40))
        self.submit.setMaximumSize(QSize(16777215, 40))
        self.submit.setStyleSheet(u"background-color: rgb(47, 70, 112);")

        self.verticalLayout.addWidget(self.submit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u7248\u672c", None))
        self.radUsd.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u6240\u4ee5USD", None))
        self.radImg.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u6240\u4ee5\u8d34\u56fe", None))
        self.submit.setText(QCoreApplication.translate("Widget", u"\u63d0\u4ea4", None))
    # retranslateUi

