# -*- coding: utf-8 -*-
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QThread,QRect

from .env import plugin_root

class MainListItem(QWidget):
    _class = 0
    def __init__(self, parent=None,label="",add_type=0) -> None:
        super().__init__(parent)
        self._anim_icon = QIcon(f"{plugin_root}/icon/anim.png")
        self._cam_icon = QIcon(f"{plugin_root}/icon/cam.png")
        self._sc_icon = QIcon(f"{plugin_root}/icon/scene.png")
        self._video_icon = QIcon(f"{plugin_root}/icon/video.png")

        self.check = QCheckBox(self)
        self.check.setCheckState(Qt.CheckState.Checked)
        self.check.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        self.check.setStyleSheet("""QCheckBox::indicator
                                    {
                                        border : 1px solid #55555533;
                                        border-radius:3px;
                                    }
                                    QCheckBox::indicator::checked
                                    {
                                        background-color:#85e9ff;
                                        border : none;
                                    }
                                    """)

        self.anim_type = QComboBox(self)
        if add_type==0:
            self.anim_type.addItem(self._anim_icon,"动画")
        elif add_type == 1:
            self.anim_type.addItem(self._cam_icon,"相机")
        elif add_type == 2:
            self.anim_type.addItem(self._video_icon,"视频")
        elif add_type == 3:
            self.anim_type.addItem(self._sc_icon,"场景")
        self._class=add_type

        self.anim_type.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Fixed)
        self.anim_type.setMaximumWidth(80)
        self.anim_type.setStyleSheet("""QComboBox{border:0;background-color: #00000000;}
                                        QComboBox::drop-down{border-style: none;}
                                    """)


        self.label = QLabel(label,self)

        self.normal = QCheckBox("N",self)
        if add_type != 0:
            self.normal.setHidden(True)
        self.normal.setCheckState(Qt.CheckState.Unchecked)
        self.normal.setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)

        self.space= QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        
        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.check,1)
        self.main_layout.addWidget(self.anim_type,2)
        self.main_layout.addWidget(self.label,10)
        self.main_layout.addItem(self.space)
        self.main_layout.addWidget(self.normal)
        self.setLayout(self.main_layout)
        self.setStyleSheet("padding:0;")