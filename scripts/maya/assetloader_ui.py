# -*- coding: utf-8 -*-
try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from PySide6.QtCore  import *
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore  import *


class Ui_AssetLoader(object):
    def setupUi(self, AssetLoader):
        if not AssetLoader.objectName():
            AssetLoader.setObjectName(u"AssetLoader")
        AssetLoader.resize(918, 630)
        self.verticalLayout = QVBoxLayout(AssetLoader)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(AssetLoader)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.proj = QComboBox(AssetLoader)
        self.proj.setObjectName(u"proj")

        self.horizontalLayout.addWidget(self.proj)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.search = QLineEdit(AssetLoader)
        self.search.setObjectName(u"search")

        self.horizontalLayout.addWidget(self.search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(AssetLoader)
        self.tabWidget.setObjectName(u"tabWidget")
        self.char = QListWidget()
        self.char.setObjectName(u"char")
        self.tabWidget.addTab(self.char, "")
        self.prop = QListWidget()
        self.prop.setObjectName(u"prop")
        self.tabWidget.addTab(self.prop, "")
        self.elem = QListWidget()
        self.elem.setObjectName(u"elem")
        self.tabWidget.addTab(self.elem, "")
        self.scene = QListWidget()
        self.scene.setObjectName(u"scene")
        self.tabWidget.addTab(self.scene, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.groupBox = QGroupBox(AssetLoader)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.groupBox.setStyleSheet(u"margin-top:20")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.BigIcon = QLabel(self.groupBox)
        self.BigIcon.setObjectName(u"BigIcon")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BigIcon.sizePolicy().hasHeightForWidth())
        self.BigIcon.setSizePolicy(sizePolicy)
        self.BigIcon.setMinimumSize(QSize(180, 180))
        self.BigIcon.setMaximumSize(QSize(180, 180))

        self.verticalLayout_2.addWidget(self.BigIcon)

        self.DisplayName = QLabel(self.groupBox)
        self.DisplayName.setObjectName(u"DisplayName")
        self.DisplayName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.DisplayName)

        self.DisplayType = QLabel(self.groupBox)
        self.DisplayType.setObjectName(u"DisplayType")
        self.DisplayType.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.DisplayType)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ImportUSD = QPushButton(self.groupBox_2)
        self.ImportUSD.setObjectName(u"ImportUSD")
        self.ImportUSD.setMinimumSize(QSize(0, 0))
        self.ImportUSD.setStyleSheet(u"padding:5")

        self.horizontalLayout_3.addWidget(self.ImportUSD)

        self.ImportMaya = QPushButton(self.groupBox_2)
        self.ImportMaya.setObjectName(u"ImportMaya")
        self.ImportMaya.setStyleSheet(u"padding:5")

        self.horizontalLayout_3.addWidget(self.ImportMaya)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.ImportRig = QPushButton(self.groupBox_2)
        self.ImportRig.setObjectName(u"ImportRig")
        self.ImportRig.setStyleSheet(u"padding:5")

        self.verticalLayout_5.addWidget(self.ImportRig)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(AssetLoader)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AssetLoader)
    # setupUi

    def retranslateUi(self, AssetLoader):
        AssetLoader.setWindowTitle(QCoreApplication.translate("AssetLoader", u"\u8d44\u4ea7\u52a0\u8f7d", None))
        self.label.setText(QCoreApplication.translate("AssetLoader", u"\u5de5\u7a0b", None))
        self.search.setPlaceholderText(QCoreApplication.translate("AssetLoader", u"\u641c\u7d22", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.char), QCoreApplication.translate("AssetLoader", u"\u89d2\u8272", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prop), QCoreApplication.translate("AssetLoader", u"\u9053\u5177", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.elem), QCoreApplication.translate("AssetLoader", u"\u5143\u7d20", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scene), QCoreApplication.translate("AssetLoader", u"\u573a\u666f", None))
        self.groupBox.setTitle(QCoreApplication.translate("AssetLoader", u"\u8be6\u7ec6\u4fe1\u606f", None))
        self.BigIcon.setText("")
        self.DisplayName.setText(QCoreApplication.translate("AssetLoader", u"\u540d\u79f0", None))
        self.DisplayType.setText(QCoreApplication.translate("AssetLoader", u"\u7c7b\u578b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AssetLoader", u"\u5bfc\u5165", None))
        self.ImportUSD.setText(QCoreApplication.translate("AssetLoader", u"\u5bfc\u5165USD", None))
        self.ImportMaya.setText(QCoreApplication.translate("AssetLoader", u"Maya\u8d44\u4ea7\u6587\u4ef6", None))
        self.ImportRig.setText(QCoreApplication.translate("AssetLoader", u"Maya\u7ed1\u5b9a", None))
    # retranslateUi


class Ui_MayaAssetDialog(object):
    def setupUi(self, MayaAssetDialog):
        if not MayaAssetDialog.objectName():
            MayaAssetDialog.setObjectName(u"MayaAssetDialog")
        MayaAssetDialog.resize(193, 85)
        self.verticalLayout = QVBoxLayout(MayaAssetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ImpClass = QComboBox(MayaAssetDialog)
        self.ImpClass.addItem("")
        self.ImpClass.addItem("")
        self.ImpClass.setObjectName(u"ImpClass")

        self.verticalLayout.addWidget(self.ImpClass)

        self.ImpType = QComboBox(MayaAssetDialog)
        self.ImpType.addItem("")
        self.ImpType.addItem("")
        self.ImpType.setObjectName(u"ImpType")

        self.verticalLayout.addWidget(self.ImpType)

        self.Submit = QPushButton(MayaAssetDialog)
        self.Submit.setObjectName(u"Submit")

        self.verticalLayout.addWidget(self.Submit)


        self.retranslateUi(MayaAssetDialog)

        QMetaObject.connectSlotsByName(MayaAssetDialog)
    # setupUi

    def retranslateUi(self, MayaAssetDialog):
        MayaAssetDialog.setWindowTitle(QCoreApplication.translate("MayaAssetDialog", u"Maya\u8d44\u4ea7\u5bfc\u5165", None))
        self.ImpClass.setItemText(0, QCoreApplication.translate("MayaAssetDialog", u"Mod\u6a21\u578b", None))
        self.ImpClass.setItemText(1, QCoreApplication.translate("MayaAssetDialog", u"Tex\u6a21\u578b", None))

        self.ImpType.setItemText(0, QCoreApplication.translate("MayaAssetDialog", u"\u53c2\u8003", None))
        self.ImpType.setItemText(1, QCoreApplication.translate("MayaAssetDialog", u"\u5bfc\u5165", None))

        self.Submit.setText(QCoreApplication.translate("MayaAssetDialog", u"\u5bfc\u5165", None))
    # retranslateUi




class Ui_MayaRigAssetDialog(object):
    def setupUi(self, MayaRigAsset):
        if not MayaRigAsset.objectName():
            MayaRigAsset.setObjectName(u"MayaRigAsset")
        MayaRigAsset.resize(357, 105)
        self.verticalLayout = QVBoxLayout(MayaRigAsset)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ImpLevel = QComboBox(MayaRigAsset)
        self.ImpLevel.addItem("")
        self.ImpLevel.addItem("")
        self.ImpLevel.addItem("")
        self.ImpLevel.setObjectName(u"ImpLevel")

        self.horizontalLayout.addWidget(self.ImpLevel)

        self.ImpType = QComboBox(MayaRigAsset)
        self.ImpType.addItem("")
        self.ImpType.addItem("")
        self.ImpType.setObjectName(u"ImpType")

        self.horizontalLayout.addWidget(self.ImpType)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Submit = QPushButton(MayaRigAsset)
        self.Submit.setObjectName(u"Submit")

        self.verticalLayout.addWidget(self.Submit)


        self.retranslateUi(MayaRigAsset)

        QMetaObject.connectSlotsByName(MayaRigAsset)
    # setupUi

    def retranslateUi(self, MayaRigAsset):
        MayaRigAsset.setWindowTitle(QCoreApplication.translate("MayaRigAsset", u"MayaRig\u5bfc\u5165", None))
        self.ImpLevel.setItemText(0, QCoreApplication.translate("MayaRigAsset", u"\u9ad8", None))
        self.ImpLevel.setItemText(1, QCoreApplication.translate("MayaRigAsset", u"\u4f4e", None))
        self.ImpLevel.setItemText(2, QCoreApplication.translate("MayaRigAsset", u"\u89d2\u8272", None))

        self.ImpType.setItemText(0, QCoreApplication.translate("MayaRigAsset", u"\u53c2\u8003", None))
        self.ImpType.setItemText(1, QCoreApplication.translate("MayaRigAsset", u"\u5bfc\u5165", None))

        self.Submit.setText(QCoreApplication.translate("MayaRigAsset", u"\u5bfc\u5165", None))
    # retranslateUi

