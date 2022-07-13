# -*- coding: utf-8 -*-
try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from PySide6.QtCore  import *
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore  import *

class Ui_QNUsdExport(object):
    def setupUi(self, QNUsdExport):
        if not QNUsdExport.objectName():
            QNUsdExport.setObjectName(u"QNUsdExport")
        QNUsdExport.resize(310, 260)
        self.verticalLayout = QVBoxLayout(QNUsdExport)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(QNUsdExport)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.start_frame = QSpinBox(self.groupBox)
        self.start_frame.setObjectName(u"start_frame")
        self.start_frame.setValue(1)
        self.start_frame.setMinimum(-10000)
        self.start_frame.setMaximum(10000)

        self.gridLayout.addWidget(self.start_frame, 0, 0, 1, 1)

        self.end_frame = QSpinBox(self.groupBox)
        self.end_frame.setObjectName(u"end_frame")
        self.end_frame.setValue(1)
        self.end_frame.setMinimum(-10000)
        self.end_frame.setMaximum(10000)

        self.gridLayout.addWidget(self.end_frame, 0, 1, 1, 1)

        self.display_color = QCheckBox(self.groupBox)
        self.display_color.setObjectName(u"display_color")

        self.gridLayout.addWidget(self.display_color, 1, 0, 1, 1)

        self.material = QCheckBox(self.groupBox)
        self.material.setObjectName(u"material")

        self.gridLayout.addWidget(self.material, 2, 0, 1, 1)

        self.uv = QCheckBox(self.groupBox)
        self.uv.setObjectName(u"uv")

        self.gridLayout.addWidget(self.uv, 3, 0, 1, 1)

        self.subdiv = QCheckBox(self.groupBox)
        self.subdiv.setObjectName(u"subdiv")

        self.gridLayout.addWidget(self.subdiv, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(QNUsdExport)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.submit = QPushButton(self.frame)
        self.submit.setObjectName(u"submit")
        self.submit.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.submit)

        self.exit = QPushButton(self.frame)
        self.exit.setObjectName(u"exit")
        self.exit.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_2.addWidget(self.exit)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(QNUsdExport)

        QMetaObject.connectSlotsByName(QNUsdExport)
    # setupUi

    def retranslateUi(self, QNUsdExport):
        QNUsdExport.setWindowTitle(QCoreApplication.translate("QNUsdExport", u"USD\u5bfc\u51fa", None))
        self.groupBox.setTitle(QCoreApplication.translate("QNUsdExport", u"\u5bfc\u51fa\u9009\u9879", None))
        self.display_color.setText(QCoreApplication.translate("QNUsdExport", u"\u5bfc\u51fa\u9876\u70b9\u989c\u8272", None))
        self.material.setText(QCoreApplication.translate("QNUsdExport", u"\u5bfc\u51fa\u6750\u8d28", None))
        self.uv.setText(QCoreApplication.translate("QNUsdExport", u"\u5bfc\u51faUV", None))
        self.subdiv.setText(QCoreApplication.translate("QNUsdExport", u"\u5bfc\u51fa\u7ec6\u5206\u6a21\u578b", None))
        self.submit.setText(QCoreApplication.translate("QNUsdExport", u"\u786e\u5b9a", None))
        self.exit.setText(QCoreApplication.translate("QNUsdExport", u"\u53d6\u6d88", None))
    # retranslateUi

