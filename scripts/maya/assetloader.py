from imp import reload
import sys,os
import json
import maya.mel as mel


_mayap = os.path.join(os.environ['QNTOOLS'],"scripts\\maya").replace("\\","/")
if _mayap not in sys.path:
    sys.path.append(_mayap)
try:
    from PySide6.QtWidgets import *
    from PySide6.QtGui import (QIcon,QPixmap)
    from PySide6.QtCore  import (QSize,Qt)
except:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import (QIcon,QPixmap)
    from PySide2.QtCore  import (QSize,Qt)
import assetloader_ui
import initconfig

reload(assetloader_ui)
reload(initconfig)

#initconfig.run()



import maya.utils as Mthread
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
maya_win= wrapInstance(int(mayaMainWindowPtr), QWidget)




import cgtw2

# def GetImages(t:cgtw2.tw,db_name:str,module_name="asset"):
#     t_id_list=t.info.get_id(db=db_name,module=module_name,filter_list=[])
#     all_data=t.info.get(db=db_name,module=module_name,id_list=t_id_list,field_sign_list=['asset.image'])
#     out_dict = dict()
#     for da in all_data:
#         try:
#             img=json.loads(da["asset.image"])
#             out_dict[da['id']]=img[0]["min"]
#         except:
#             out_dict[da['id']]=None
#     return out_dict

def GetImages(t:cgtw2.tw,db_name:str,module_name="asset"):
    t_id_list=t.info.get_id(db=db_name,module=module_name,filter_list=[])
    all_data=t.info.download_image(db=db_name, module=module_name, id_list=t_id_list, field_sign="asset.image", is_small=True)
    out_dict = dict()
    for da in all_data:
        out_dict[da['id']]=da["asset.image"]
    return out_dict

class MyMayaAssetDiglog(QDialog):
    def __init__(self,parent=None,mod_file=None,tex_file=None):
        super(MyMayaAssetDiglog,self).__init__(parent)

        self.ui = assetloader_ui.Ui_MayaAssetDialog()
        self.ui.setupUi(self)
        self.mod_file = mod_file
        self.tex_file = tex_file

        self.ui.Submit.clicked.connect(self.run)
    def run(self):
        if self.ui.ImpClass.currentIndex() == 0:
            if self.ui.ImpType.currentIndex() == 0:
                mel.eval(f'file -r -type "mayaAscii"  -ignoreVersion -gl  -namespace "{os.path.basename(self.mod_file)}" -options "v=0;" "{self.mod_file}";')
            else:
                mel.eval(f'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "{self.mod_file}";')
        else:
            if self.ui.ImpType.currentIndex() == 0:
                mel.eval(f'file -r -type "mayaAscii"  -ignoreVersion -gl  -namespace "{os.path.basename(self.tex_file)}" -options "v=0;" "{self.tex_file}";')
            else:
                mel.eval(f'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "{self.tex_file}";')
        self.accept()
    
class MyMayaRigAssetDiglog(QDialog):
    def __init__(self,parent=None,rig_l=None,rig_h=None,rig_c=None):
        super(MyMayaRigAssetDiglog,self).__init__(parent)

        self.ui = assetloader_ui.Ui_MayaRigAssetDialog()
        self.ui.setupUi(self)

        self.rig_l = rig_l
        self.rig_h = rig_h
        self.rig_c = rig_c
        self.ui.Submit.clicked.connect(self.run)
    def run(self):
        if self.ui.ImpLevel.currentIndex() == 0:
            rig_file = self.rig_h
            if os.path.exists(rig_file):
                if self.ui.ImpType.currentIndex() == 0:
                    mel.eval(f'file -r -type "mayaAscii"  -ignoreVersion -gl  -namespace "{os.path.basename(rig_file)}" -options "v=0;" "{rig_file}";')
                else:
                    mel.eval(f'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "{rig_file}";')
            else:
                QMessageBox.warning(self,"提示","绑定文件不存在")
        elif self.ui.ImpLevel.currentIndex() == 1:
            rig_file = self.rig_l
            if os.path.exists(rig_file):
                if self.ui.ImpType.currentIndex() == 0:
                    mel.eval(f'file -r -type "mayaAscii"  -ignoreVersion -gl  -namespace "{os.path.basename(rig_file)}" -options "v=0;" "{rig_file}";')
                else:
                    mel.eval(f'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "{rig_file}";')
            else:
                QMessageBox.warning(self,"提示","绑定文件不存在")
        elif self.ui.ImpLevel.currentIndex() == 2:
            rig_file = self.rig_c
            if os.path.exists(rig_file):
                if self.ui.ImpType.currentIndex() == 0:
                    mel.eval(f'file -r -type "mayaAscii"  -ignoreVersion -gl  -namespace "{os.path.basename(rig_file)}" -options "v=0;" "{rig_file}";')
                else:
                    mel.eval(f'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "{rig_file}";')
            else:
                QMessageBox.warning(self,"提示","绑定文件不存在")
        

class MyWin(QWidget):
    def __init__(self,parent=None):
        super(MyWin,self).__init__(parent)

        self.ui = assetloader_ui.Ui_AssetLoader()
        self.ui.setupUi(self)
        self.icons=dict()
        self.current_data = None

        self.initCGTW()
        self.init()

        self.ui.proj.currentIndexChanged.connect(self.changeProject)
        self.ui.search.textChanged.connect(self.changeSearch)

        self.ui.char.itemClicked.connect(self.clickIcon)
        self.ui.prop.itemClicked.connect(self.clickIcon)
        self.ui.elem.itemClicked.connect(self.clickIcon)
        self.ui.scene.itemClicked.connect(self.clickIcon)

        self.ui.ImportUSD.clicked.connect(self.clickUSDAsset)
        self.ui.ImportMaya.clicked.connect(self.clickMayaAsset)
        self.ui.ImportRig.clicked.connect(self.clickMayaRig)
    def initCGTW(self):
        self.t_tw = cgtw2.tw()
    def init(self):
        self.setViewMode(0)
        self.initProj()
    
    def setViewMode(self,mode=0):
        if mode==0:
            self.ui.char.setViewMode(QListView.IconMode)
            self.ui.char.setGridSize(QSize(65,80))
            self.ui.char.setIconSize(QSize(60,60))

            self.ui.prop.setViewMode(QListView.IconMode)
            self.ui.prop.setGridSize(QSize(65,80))
            self.ui.prop.setIconSize(QSize(60,60))
            
            self.ui.elem.setViewMode(QListView.IconMode)
            self.ui.elem.setGridSize(QSize(65,80))
            self.ui.elem.setIconSize(QSize(60,60))

            self.ui.scene.setViewMode(QListView.IconMode)
            self.ui.scene.setGridSize(QSize(65,80))
            self.ui.scene.setIconSize(QSize(60,60))
        else:
            self.ui.char.setViewMode(QListView.ListMode)
            self.ui.prop.setViewMode(QListView.ListMode)
            self.ui.elem.setViewMode(QListView.ListMode)
            self.ui.scene.setViewMode(QListView.ListMode)
    def initProj(self):
        t_id_list =  self.t_tw.info.get_id(db='public', module='project', filter_list=[['project.status','=','Active']])
        self.t_projs = self.t_tw.info.get(db='public', module='project', id_list=t_id_list, field_sign_list=['project.entity','project.database','project.template','project.full_name'])

        #init proj
        for p in self.t_projs:
            # {'project.entity': 'LDSF', 'project.database': 'proj_ldsf', 'id': '1A99F25C-BACA-442D-9892-8A8CD11DA2D3'}
            a=self.ui.proj.addItem(f'{p["project.full_name"]}({p["project.entity"]})',userData=p)
        
        self.changeProject()
    def changeProject(self,idx=0):
        p=self.ui.proj.currentData()
        if p != None:
            self.icons=GetImages(self.t_tw,p['project.database'])
            self.ui.scene.clear()
            self.ui.char.clear()
            self.ui.elem.clear()
            self.ui.prop.clear()

            t_id_list=self.t_tw.info.get_id(db=p['project.database'],module='asset',filter_list=[])
            a=self.t_tw.info.get(db=p['project.database'],module='asset',id_list=t_id_list,field_sign_list=['asset.entity','asset.cn_name','asset.link_asset_type'])

            for i in a:
                    # [{'asset.entity': 'tabel', 'id': '50CE5D5B-03C5-54A4-2AF2-A02E777430FB'}]
                    if i['asset.link_asset_type'] == "Sets":
                        img_path = initconfig.icon_path2(i['id'],self.icons,"scene.png")
                        item = QListWidgetItem(QIcon(img_path),i['asset.entity'])
                        item.setData(3,i)
                        item.setData(4,img_path)
                        self.ui.scene.addItem(item)
                    elif i['asset.link_asset_type'] == "Chars":
                        img_path = initconfig.icon_path2(i['id'],self.icons,"char.png")
                        item = QListWidgetItem(QIcon(img_path),i['asset.entity'])
                        item.setData(3,i)
                        item.setData(4,img_path)
                        self.ui.char.addItem(item)

                    elif i['asset.link_asset_type'] == "Props":
                        img_path = initconfig.icon_path2(i['id'],self.icons,"prop.png")
                        item = QListWidgetItem(QIcon(img_path),i['asset.entity'])
                        item.setData(3,i)
                        item.setData(4,img_path)
                        self.ui.prop.addItem(item)

                    elif i['asset.link_asset_type'] == "Elements":
                        img_path = initconfig.icon_path2(i['id'],self.icons,"elem.png")
                        item = QListWidgetItem(QIcon(img_path),i['asset.entity'])
                        item.setData(3,i)
                        item.setData(4,img_path)
                        self.ui.elem.addItem(item)
    
    def changeSearch(self):
        if len(self.ui.search.text()) < 0:
            for c_idx in range(self.ui.char.count()):
                c=self.ui.char.item(c_idx)
                c.setHidden(False)
            for c_idx in range(self.ui.elem.count()):
                c=self.ui.elem.item(c_idx)
                c.setHidden(False)
            for c_idx in range(self.ui.prop.count()):
                c=self.ui.prop.item(c_idx)
                c.setHidden(False)
            for c_idx in range(self.ui.scene.count()):
                c=self.ui.scene.item(c_idx)
                c.setHidden(False)

        else:
            t = self.ui.search.text()

            for c_idx in range(self.ui.char.count()):
                c=self.ui.char.item(c_idx)
                if t not in c.text() and t not in c.data(3)['asset.cn_name']:
                    c.setHidden(True)
                else:
                    c.setHidden(False)

            for c_idx in range(self.ui.elem.count()) and t not in c.data(3)['asset.cn_name']:
                c=self.ui.elem.item(c_idx)
                if t not in c.text():
                    c.setHidden(True)
                else:
                    c.setHidden(False)
            
            for c_idx in range(self.ui.prop.count()) and t not in c.data(3)['asset.cn_name']:
                c=self.ui.prop.item(c_idx)
                if t not in c.text():
                    c.setHidden(True)
                else:
                    c.setHidden(False)
            
            for c_idx in range(self.ui.scene.count()) and t not in c.data(3)['asset.cn_name']:
                c=self.ui.scene.item(c_idx)
                if t not in c.text():
                    c.setHidden(True)
                else:
                    c.setHidden(False)

    def clickIcon(self,idx:QListWidgetItem):
        try:
            self.ui.BigIcon.setPixmap(QPixmap(idx.data(4)))
            self.ui.DisplayName.setText(f"{idx.data(3)['asset.cn_name']}({idx.data(3)['asset.entity']})"[:10])
            self.ui.DisplayType.setText(idx.data(3)['asset.link_asset_type'])
            self.current_data = idx.data(3)
            
            
        except:
            pass
    
    def currentDataIsNone(self)->bool:
        if self.current_data == None:
            QMessageBox.warning(self,"警告","你未选择资产，请选择资产后操作")
            return False
        return True

    def clickUSDAsset(self):
        if not self.currentDataIsNone():
            return
        try:
            dir=self.t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=[self.current_data['id']],folder_sign_list=["asset"])[0]['asset']
            usd_file_path = os.path.join(dir,"USD",f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}.usd").replace("\\","/")

            if os.path.exists(usd_file_path.replace("/","\\")):
                mel.eval(f'file -import -type "USD Import"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options ";shadingMode=[[useRegistry,rendermanForMaya],[pxrRis,none],[useRegistry,UsdPreviewSurface],[displayColor,none],[none,none]];preferredMaterial=lambert;primPath=/;readAnimData=1;useCustomFrameRange=0;startTime=0;endTime=0;importUSDZTextures=0"  -pr  -importFrameRate true  -importTimeRange "override" "{usd_file_path}";')
            else:
                QMessageBox.warning(self,"警告","该USD资产不存在！")
        except:
            QMessageBox.warning(self,"警告","该项目不存在USD资产！")
        #file -import -type "USD Import"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options ";shadingMode=[[useRegistry,rendermanForMaya],[pxrRis,none],[useRegistry,UsdPreviewSurface],[displayColor,none],[none,none]];preferredMaterial=lambert;primPath=/;readAnimData=1;useCustomFrameRange=0;startTime=0;endTime=0;importUSDZTextures=0"  -pr  -importFrameRate true  -importTimeRange "override" "D:/GBWZ/AssetsRoot/USDAssets/Assets/chr_c1007yylb/chr_c1007yylb_Assets.usd";
    def clickMayaAsset(self):
        if not self.currentDataIsNone():
            return
        try:
            mod_dir=self.t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=[self.current_data['id']],folder_sign_list=["mod_maya"])[0]['mod_maya']
            mod_maya_file_path = os.path.join(mod_dir,f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}_mod.ma").replace("\\","/")

            tex_dir=self.t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=[self.current_data['id']],folder_sign_list=["tex_maya"])[0]['tex_maya']
            tex_maya_file_path = os.path.join(tex_dir,f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}_tex.ma").replace("\\","/")

            if os.path.exists(mod_maya_file_path.replace("/","\\")) or os.path.exists(tex_maya_file_path.replace("/","\\")):
                dia = MyMayaAssetDiglog(self,mod_file=mod_maya_file_path,tex_file=tex_maya_file_path)
                dia.exec_()
            else:
                QMessageBox.warning(self,"警告","该Maya资产不存在！")
        except:
            QMessageBox.warning(self,"警告","该项目不存在Maya资产！")
        
    def clickMayaRig(self):
        if not self.currentDataIsNone():
            return
        try:
            dir=self.t_tw.info.get_dir(db=self.ui.proj.currentData()['project.database'],module='asset',id_list=[self.current_data['id']],folder_sign_list=["maya_rig"])[0]['maya_rig']
            
            l = os.path.join(dir,f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}_rig_l.ma").replace("\\","/")
            h = os.path.join(dir,f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}_rig_h.ma").replace("\\","/")
            c = os.path.join(dir,f"{self.current_data['asset.link_asset_type']}_{self.current_data['asset.entity']}_rig_c.ma").replace("\\","/")

            dia = MyMayaRigAssetDiglog(self,rig_l= l,rig_h=h,rig_c=c)
            dia.exec_()
        except:
            QMessageBox.warning(self,"警告","该项目不存在绑定资产！")

def run():
    a=MyWin()
    a.setParent(maya_win)
    a.setWindowFlag(Qt.Window)
    a.show()

if __name__ == "__main__":
    a=MyWin()
    a.setParent(maya_win)
    a.setWindowFlag(Qt.Window)
    a.show()