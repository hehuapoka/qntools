# -*- coding: utf-8 -*-
from genericpath import isfile
import sys,json,os
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from submitasset_ui import Ui_Widget

#init
plugin_root = os.environ['QNTOOLS']
sys.path.append(os.path.dirname(__file__)+"/..")
sys.path.append(os.path.join(os.environ['CGTEAMWORK_LOCATION'],"bin\\base").replace("\\","//"))

# import cgtw2
# t_tw = cgtw2.tw()




class MainWin(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.init()

    def init(self):
        a = [".usd",".usda",".usdc"]
        for i in os.listdir(".\\"):
            if not os.path.isfile(i):
                continue
            if os.path.splitext(i)[-1] not in a:
                continue
            k=QListWidgetItem(i,self.ui.usd)
            k.setCheckState(Qt.CheckState.Checked)

        if not os.path.exists(".\\Textures"): return

        for i in os.listdir(".\\Textures"):
            if not os.path.isfile(".\\Textures\\"+i):
                continue
            if os.path.splitext(i)[-1] != ".tx":
                continue
            k=QListWidgetItem(i,self.ui.img)
            k.setCheckState(Qt.CheckState.Checked)

            


if __name__ == "__main__":
    app= QApplication()
    win = MainWin()
    win.setWindowIcon(QIcon(f"{plugin_root}/icon/asset.png"))
    win.show()
    sys.exit(app.exec())
